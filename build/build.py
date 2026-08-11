#!/usr/bin/env python3
"""
Build the AI Chief of Staff package for every supported AI tool from one source tree.

Everything in dist/, plugin/skills/, and the repo-root docs is GENERATED.
Edit src/ instead, then run:  python3 build/build.py

Created by The NoW of Work. MIT licensed. Yours to edit.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
PLUGIN = ROOT / "plugin"

PLATFORMS = ("claude", "chatgpt")

MANUAL_NAME = {
    "claude": "CLAUDE.md",
    "chatgpt": "PROJECT-INSTRUCTIONS.md",
}

# Workspace files, in the order a human would meet them.
# key = source stem, value = filename in the built workspace
WORKSPACE_FILES = [
    ("_manual", None),  # filename resolved per platform
    ("about-me", "about-me.md"),
    ("my-work", "my-work.md"),
    ("tomorrow", "tomorrow.md"),
    ("commitments", "commitments.md"),
    # the decision ledger sits next to the commitment ledger, on purpose
    ("decisions", "decisions.md"),
    ("connections", "connections.md"),
]

OUTPUT_FOLDERS = ["briefs", "meetings", "people", "archive"]

# Docs from src/docs/ that ride inside the workspace itself.
# The leader is handed the workspace folder, not the repo, so a page they are
# told to read has to sit in the folder they can actually open. These are
# reading material, so they stay out of WORKSPACE_FILES and out of the reading
# order: nothing should load them on every run. They still hold {{VERSION}},
# so they are rendered like the context files rather than copied like example/.
WORKSPACE_DOCS = ["QUICK-START.md"]

# Docs that get one render per platform, into docs/claude/ and docs/chatgpt/.
# A consultant deploys to one platform and should never read the other's paths.
# The filenames are identical in both directories on purpose: every cross-link
# between docs is a bare filename, so it resolves inside whichever directory the
# reader is already in and no link has to know which platform it is on.
PLATFORM_DOCS = [
    "READ-ME-FIRST.md",
    "SCHEDULES.md",
    "DEPLOY-FOR-A-CLIENT.md",
]

# Everything else in src/docs/ renders once, to the repo root. README.md is the
# GitHub landing page and routes to the two sets. QUICK-START.md is handed to the
# leader and already ships per-platform inside each workspace, per WORKSPACE_DOCS.
DOCS = ROOT / "docs"

# the worked reference workspace, copied rather than rendered
EXAMPLE_SRC = SRC / "example"

MAX_DESCRIPTION = 200


# ----------------------------------------------------------------------------
# rendering
# ----------------------------------------------------------------------------

BLOCK_RE = re.compile(r"\{\{#(claude|chatgpt)\}\}(.*?)\{\{/\1\}\}", re.DOTALL)


def render(text: str, platform: str, version: str) -> str:
    """Resolve platform blocks and tokens."""

    def keep(match: re.Match) -> str:
        return match.group(2) if match.group(1) == platform else ""

    out = BLOCK_RE.sub(keep, text)
    out = out.replace("{{MANUAL}}", MANUAL_NAME[platform])
    out = out.replace("{{VERSION}}", version)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.strip() + "\n"


FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)


def parse_behaviour(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(raw)
    if not match:
        fail(f"{path.name}: missing YAML frontmatter")
    meta: dict = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"{path.name}: cannot parse frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    for required in ("name", "order", "description"):
        if required not in meta:
            fail(f"{path.name}: frontmatter missing '{required}'")
    meta["order"] = int(meta["order"])
    meta["body"] = match.group(2)
    meta["source"] = path.name
    return meta


def fail(message: str) -> None:
    print(f"BUILD FAILED: {message}", file=sys.stderr)
    raise SystemExit(1)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def escape_yaml(value: str) -> str:
    """Quote a frontmatter scalar safely."""
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


# ----------------------------------------------------------------------------
# workspace
# ----------------------------------------------------------------------------


def build_workspace(dest: Path, platform: str, version: str) -> None:
    """Write the seven context files, the four output folders, and the
    workspace docs into dest."""
    for stem, filename in WORKSPACE_FILES:
        src_path = SRC / "workspace" / f"{stem}.md"
        target = filename or MANUAL_NAME[platform]
        write(dest / target, render(src_path.read_text(encoding="utf-8"), platform, version))

    for folder in OUTPUT_FOLDERS:
        src_path = SRC / "workspace" / "folders" / f"{folder}.md"
        write(
            dest / folder / "README.md",
            render(src_path.read_text(encoding="utf-8"), platform, version),
        )

    for name in WORKSPACE_DOCS:
        src_path = SRC / "docs" / name
        if not src_path.is_file():
            fail(f"src/docs/{name} is missing, so the workspace cannot carry it")
        write(dest / name, render(src_path.read_text(encoding="utf-8"), platform, version))


def copy_example(dest: Path) -> None:
    """Copy the worked reference workspace into dest, byte for byte.

    This one does not go through render(). The example is finished text written
    for a leader to read, so a token in it would be a mistake rather than a slot,
    and both packs are meant to carry the identical files. Dotfiles are skipped
    because macOS leaves them lying around and they are not part of the example.
    """
    if not EXAMPLE_SRC.is_dir():
        fail("src/example/ is missing, so there is no worked example to ship")
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(EXAMPLE_SRC, dest, ignore=shutil.ignore_patterns(".*"))


# ----------------------------------------------------------------------------
# validation
# ----------------------------------------------------------------------------


def validate(behaviours: list[dict]) -> None:
    seen_names: set[str] = set()
    seen_orders: set[int] = set()
    for b in behaviours:
        desc_len = len(b["description"])
        if desc_len > MAX_DESCRIPTION:
            fail(
                f"{b['source']}: description is {desc_len} characters, "
                f"limit is {MAX_DESCRIPTION}"
            )
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", b["name"]):
            fail(f"{b['source']}: name {b['name']!r} must be kebab-case")
        if b["name"] in seen_names:
            fail(f"duplicate behaviour name: {b['name']}")
        if b["order"] in seen_orders:
            fail(f"duplicate order: {b['order']}")
        seen_names.add(b["name"])
        seen_orders.add(b["order"])
    print(f"  validated {len(behaviours)} behaviours, longest description "
          f"{max(len(b['description']) for b in behaviours)} chars")


# ----------------------------------------------------------------------------
# Claude
# ----------------------------------------------------------------------------


def build_claude(behaviours: list[dict], version: str) -> None:
    platform = "claude"
    skills_root = PLUGIN / "skills"
    if skills_root.exists():
        shutil.rmtree(skills_root)

    workspace = DIST / "claude" / "ai-chief-of-staff"
    if (DIST / "claude").exists():
        shutil.rmtree(DIST / "claude")

    build_workspace(workspace, platform, version)
    copy_example(workspace / "example")

    uploads = DIST / "claude" / "skill-uploads"
    uploads.mkdir(parents=True, exist_ok=True)

    for b in behaviours:
        front = (
            "---\n"
            f"name: {b['name']}\n"
            f"description: {escape_yaml(b['description'])}\n"
            "---\n\n"
        )
        body = render(b["body"], platform, version)
        skill_md = front + body

        # 1. into the plugin
        write(skills_root / b["name"] / "SKILL.md", skill_md)
        # 2. into the drop-in workspace copy
        write(workspace / "skills" / b["name"] / "SKILL.md", skill_md)

        # onboarding carries the blank workspace templates so it can scaffold
        if b["name"] == "onboarding":
            for target_root in (skills_root / b["name"], workspace / "skills" / b["name"]):
                build_workspace(target_root / "templates", platform, version)

    # one zip per skill, each containing the skill DIRECTORY
    for b in behaviours:
        zip_path = uploads / f"{b['name']}.zip"
        base = skills_root / b["name"]
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for path in sorted(base.rglob("*")):
                if path.is_file():
                    zf.write(path, Path(b["name"]) / path.relative_to(base))

    print(f"  claude: {len(behaviours)} skills, workspace, example, "
          f"{len(behaviours)} upload zips")


# ----------------------------------------------------------------------------
# ChatGPT
# ----------------------------------------------------------------------------

CHATGPT_PROMPT_HEADER = """> **{name}**. {description}
>
> **How to use this file.** Paste the whole thing into the chat when you want
> this behaviour, or keep all of these in the project so you can say
> "run {name}" and point at the file. The project instructions
> (`PROJECT-INSTRUCTIONS.md`) must already be set, because every behaviour
> assumes it has been read.
>
> ChatGPT cannot write to your folders on its own. Anywhere this file says
> "save" or "write", produce the file contents in a code block and let the
> leader paste it back into the project.

---

"""


def build_chatgpt(behaviours: list[dict], version: str) -> None:
    platform = "chatgpt"
    out = DIST / "chatgpt"
    if out.exists():
        shutil.rmtree(out)

    build_workspace(out / "workspace", platform, version)
    copy_example(out / "example")

    # the operating manual is pasted into the project's custom instructions,
    # so put a copy where a human will trip over it first
    shutil.copy2(
        out / "workspace" / MANUAL_NAME[platform],
        out / MANUAL_NAME[platform],
    )

    for b in behaviours:
        header = CHATGPT_PROMPT_HEADER.format(
            name=b["name"], description=b["description"]
        )
        body = render(b["body"], platform, version)
        write(out / "prompts" / f"{b['order']}-{b['name']}.md", header + body)

    print(f"  chatgpt: {len(behaviours)} prompts, workspace, example")


# ----------------------------------------------------------------------------
# docs and release zip
# ----------------------------------------------------------------------------


def build_docs(version: str) -> None:
    """Write the docs, splitting the ones whose reader only needs one platform."""
    if DOCS.exists():
        shutil.rmtree(DOCS)

    shared = split = 0
    for path in sorted((SRC / "docs").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if path.name in PLATFORM_DOCS:
            for platform in PLATFORMS:
                write(DOCS / platform / path.name, render(text, platform, version))
            split += 1
        else:
            # Shared docs are Claude-flavoured, so any ChatGPT specifics in them
            # have to be written as plain prose rather than in a platform block.
            write(ROOT / path.name, render(text, "claude", version))
            shared += 1

    missing = [name for name in PLATFORM_DOCS if not (SRC / "docs" / name).is_file()]
    if missing:
        fail(f"PLATFORM_DOCS names files that are not in src/docs/: {missing}")

    print(f"  docs: {shared} shared at the root, {split} split across "
          f"{len(PLATFORMS)} platforms in docs/")


def build_release_zip(version: str) -> None:
    zip_path = DIST / f"ai-chief-of-staff-v{version}.zip"
    # A zip from an older VERSION sitting beside this one is a trap. There is
    # nothing on the file listing that says which is current, so whoever picks
    # the wrong one deploys a release without any of this in it. Only the zip
    # matching VERSION survives.
    for stale in sorted(DIST.glob("ai-chief-of-staff-v*.zip")):
        if stale != zip_path:
            stale.unlink()
            print(f"  release: removed stale {stale.name}")
    if zip_path.exists():
        zip_path.unlink()
    # The docs are whatever build_docs() just wrote, so ask src/docs/ rather
    # than listing filenames here. A new doc used to need a second edit in this
    # function, and forgetting it dropped the doc from the release silently.
    # The split ones live under docs/ and are picked up by that directory below.
    include = [
        ROOT / path.name
        for path in sorted((SRC / "docs").glob("*.md"))
        if path.name not in PLATFORM_DOCS
    ]
    include += [
        ROOT / "LICENSE",
        DOCS,              # per-platform READ-ME-FIRST, SCHEDULES, DEPLOY
        DIST / "claude",   # workspace, skills, upload zips, example
        DIST / "chatgpt",  # workspace, prompts, example
    ]
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for item in include:
            if not item.exists():
                fail(f"release zip: {item.relative_to(ROOT)} was never built")
            if item.is_file():
                zf.write(item, Path("ai-chief-of-staff") / item.name)
            else:
                for path in sorted(item.rglob("*")):
                    if path.is_file():
                        zf.write(path, Path("ai-chief-of-staff") / path.relative_to(ROOT))
    size = zip_path.stat().st_size / 1024
    print(f"  release: {zip_path.name} ({size:.0f} KB)")


def sync_versions(version: str) -> None:
    """Keep the plugin and marketplace manifests on the same version as VERSION."""
    for manifest in (
        ROOT / ".claude-plugin" / "marketplace.json",
        PLUGIN / ".claude-plugin" / "plugin.json",
    ):
        if not manifest.exists():
            continue
        data = json.loads(manifest.read_text(encoding="utf-8"))
        if "plugins" in data:
            for entry in data["plugins"]:
                entry["version"] = version
        else:
            data["version"] = version
        write(manifest, json.dumps(data, indent=2) + "\n")
    print("  manifests: version synced")


# ----------------------------------------------------------------------------


def main() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    print(f"Building AI Chief of Staff v{version}")

    behaviours = sorted(
        (parse_behaviour(p) for p in (SRC / "behaviours").glob("*.md")),
        key=lambda b: b["order"],
    )
    if not behaviours:
        fail("no behaviours found in src/behaviours/")

    validate(behaviours)
    build_claude(behaviours, version)
    build_chatgpt(behaviours, version)
    build_docs(version)
    sync_versions(version)
    build_release_zip(version)

    print("Done.")


if __name__ == "__main__":
    main()
