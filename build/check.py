#!/usr/bin/env python3
"""
Verify the built package. Run after build/build.py:

    python3 build/check.py     # or: make check

Every check below has failed at least once in some version of a package like
this one, which is why it is a check and not a comment.
"""

from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
PLUGIN = ROOT / "plugin"

MAX_DESCRIPTION = 200
EXPECTED_BEHAVIOURS = {
    "onboarding",
    "morning-brief",
    "meeting-prep",
    "transcript-to-actions",
    "daily-transcript-sweep",
    "end-of-day-close",
    "weekly-review",
    "connection-check",
}
WORKSPACE_FILES = {"about-me.md", "my-work.md", "tomorrow.md", "commitments.md", "connections.md"}
OUTPUT_FOLDERS = {"briefs", "meetings", "people", "archive"}

failures: list[str] = []
checks = 0


def check(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        failures.append(message)


def main() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

    # 1. no unresolved template tokens anywhere in the shipped output
    token = re.compile(r"\{\{[#/]?[A-Za-z_]+\}\}")
    for base in (DIST, PLUGIN / "skills", ROOT / "READ-ME-FIRST.md", ROOT / "README.md",
                 ROOT / "CREDITS.md", ROOT / "CHANGELOG.md"):
        paths = [base] if base.is_file() else sorted(base.rglob("*.md"))
        for path in paths:
            text = path.read_text(encoding="utf-8")
            # a token inside backticks is documentation of the syntax, not a miss
            text = re.sub(r"`[^`\n]*`", "", text)
            hits = token.findall(text)
            check(not hits, f"unresolved token(s) {sorted(set(hits))} in {path.relative_to(ROOT)}")

    # 2. plugin skills: frontmatter, name match, description length
    skills_dir = PLUGIN / "skills"
    found = {p.name for p in skills_dir.iterdir() if p.is_dir()}
    check(found == EXPECTED_BEHAVIOURS,
          f"plugin skills mismatch: missing {EXPECTED_BEHAVIOURS - found}, extra {found - EXPECTED_BEHAVIOURS}")

    for name in sorted(found):
        skill_md = skills_dir / name / "SKILL.md"
        check(skill_md.exists(), f"{name}: no SKILL.md")
        if not skill_md.exists():
            continue
        text = skill_md.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        check(bool(match), f"{name}: SKILL.md has no frontmatter")
        if not match:
            continue
        front = match.group(1)
        name_line = re.search(r"^name:\s*(.+)$", front, re.M)
        desc_line = re.search(r'^description:\s*"(.*)"$', front, re.M)
        check(bool(name_line) and name_line.group(1).strip() == name,
              f"{name}: frontmatter name does not match folder name")
        check(bool(desc_line), f"{name}: description is not a quoted scalar")
        if desc_line:
            length = len(desc_line.group(1))
            check(length <= MAX_DESCRIPTION,
                  f"{name}: description is {length} chars, limit {MAX_DESCRIPTION}")

    # 3. onboarding carries the templates it needs to scaffold a workspace
    templates = skills_dir / "onboarding" / "templates"
    check(templates.is_dir(), "onboarding: templates/ missing")
    if templates.is_dir():
        names = {p.name for p in templates.iterdir()}
        check(WORKSPACE_FILES | {"CLAUDE.md"} <= names,
              f"onboarding templates missing: {(WORKSPACE_FILES | {'CLAUDE.md'}) - names}")
        check(OUTPUT_FOLDERS <= names,
              f"onboarding templates missing folders: {OUTPUT_FOLDERS - names}")

    # 4. upload zips contain the skill DIRECTORY, not loose files
    uploads = DIST / "claude" / "skill-uploads"
    zips = sorted(uploads.glob("*.zip"))
    check({z.stem for z in zips} == EXPECTED_BEHAVIOURS, "one upload zip per behaviour")
    for z in zips:
        with zipfile.ZipFile(z) as zf:
            entries = zf.namelist()
        check(f"{z.stem}/SKILL.md" in entries,
              f"{z.name}: must contain {z.stem}/SKILL.md at the top level")
        check(all(e.startswith(f"{z.stem}/") for e in entries),
              f"{z.name}: contains files outside the {z.stem}/ directory")

    # 5. the drop-in Claude workspace is complete
    ws = DIST / "claude" / "ai-chief-of-staff"
    for f in WORKSPACE_FILES | {"CLAUDE.md"}:
        check((ws / f).is_file(), f"claude workspace missing {f}")
    for d in OUTPUT_FOLDERS:
        check((ws / d / "README.md").is_file(), f"claude workspace missing {d}/README.md")
    check({p.name for p in (ws / "skills").iterdir()} == EXPECTED_BEHAVIOURS,
          "claude workspace skills/ incomplete")

    # 6. the ChatGPT pack is complete
    cg = DIST / "chatgpt"
    check((cg / "PROJECT-INSTRUCTIONS.md").is_file(),
          "chatgpt: PROJECT-INSTRUCTIONS.md missing from the top level")
    for f in WORKSPACE_FILES | {"PROJECT-INSTRUCTIONS.md"}:
        check((cg / "workspace" / f).is_file(), f"chatgpt workspace missing {f}")
    prompts = {p.stem.split("-", 1)[1] for p in (cg / "prompts").glob("*.md")}
    check(prompts == EXPECTED_BEHAVIOURS,
          f"chatgpt prompts mismatch: {EXPECTED_BEHAVIOURS ^ prompts}")

    # 7. the two versions say the same things about the same subjects
    for name in sorted(EXPECTED_BEHAVIOURS):
        claude_text = (skills_dir / name / "SKILL.md").read_text(encoding="utf-8")
        cg_path = next((cg / "prompts").glob(f"*-{name}.md"))
        cg_text = cg_path.read_text(encoding="utf-8")
        claude_heads = set(re.findall(r"^##+ .+$", claude_text, re.M))
        cg_heads = set(re.findall(r"^##+ .+$", cg_text, re.M))
        check(claude_heads == cg_heads,
              f"{name}: Claude and ChatGPT versions have drifted: {claude_heads ^ cg_heads}")

    # 8. manifests parse, and versions agree with VERSION
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    plug = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text())
    check(market.get("name") and market.get("owner") and market.get("plugins"),
          "marketplace.json missing a required field")
    check(plug.get("name") == "ai-chief-of-staff", "plugin.json name is wrong")
    check(plug.get("version") == version, f"plugin.json version != VERSION ({version})")
    for entry in market["plugins"]:
        check(entry.get("version") == version,
              f"marketplace entry {entry.get('name')} version != VERSION ({version})")
        src = entry.get("source")
        check(isinstance(src, str) and (ROOT / src.lstrip("./")).is_dir(),
              f"marketplace entry {entry.get('name')}: source {src!r} does not exist")

    # 9. nothing client-specific or version-historical leaked into the output
    banned = re.compile(
        r"\b(conan|ashleah|rocky|nanaimo|mackay|peterson|whitewater"
        r"|v[2-9]\s*:|previous version|earlier version)\b",
        re.I,
    )
    for path in sorted(DIST.rglob("*.md")) + sorted((PLUGIN / "skills").rglob("*.md")):
        hits = banned.findall(path.read_text(encoding="utf-8"))
        check(not hits, f"{path.relative_to(ROOT)}: client-specific or historical reference {hits}")

    # 10. the release zip exists and unzips to one folder
    release = DIST / f"ai-chief-of-staff-v{version}.zip"
    check(release.is_file(), f"release zip {release.name} missing")
    if release.is_file():
        with zipfile.ZipFile(release) as zf:
            roots = {e.split("/")[0] for e in zf.namelist()}
        check(roots == {"ai-chief-of-staff"},
              f"release zip should unzip to one folder, got {roots}")

    if failures:
        print(f"FAILED {len(failures)} of {checks} checks:\n")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print(f"All {checks} checks passed.")


if __name__ == "__main__":
    main()
