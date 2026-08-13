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
SRC = ROOT / "src"
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
    "inbox-triage",
    "chase",
    "decision-brief",
    "recall",
    "health-check",
}
WORKSPACE_FILES = {
    "about-me.md",
    "my-work.md",
    "tomorrow.md",
    "commitments.md",
    "decisions.md",
    "connections.md",
}
OUTPUT_FOLDERS = {"briefs", "meetings", "people", "archive"}

# Docs that must sit inside the workspace, not only at the repo root.
# READ-ME-FIRST tells the consultant to hand the leader this page, and a
# consultant who installs from a zip never downloads the repo, so a root-only
# copy is a page nobody can hand over.
WORKSPACE_DOCS = {"QUICK-START.md"}

# Docs that render once per platform into docs/claude/ and docs/chatgpt/ rather
# than once to the repo root. A consultant deploys to one platform and should
# never have to read the other one's paths to find their own.
PLATFORM_DOCS = {
    "READ-ME-FIRST.md",
    "SCHEDULES.md",
    "DEPLOY-FOR-A-CLIENT.md",
}
DOCS = ROOT / "docs"

# what the leader's folder actually is on each platform. The "What is in the
# folder" tree in READ-ME-FIRST describes this directory and nothing else.
WORKSPACE_ROOTS = {
    "claude": DIST / "claude" / "ai-chief-of-staff",
    "chatgpt": DIST / "chatgpt" / "workspace",
}

# where the worked example lands in each pack, and the folders it must fill
EXAMPLE_ROOTS = (
    DIST / "claude" / "ai-chief-of-staff" / "example",
    DIST / "chatgpt" / "example",
)
EXAMPLE_FOLDERS = {"briefs", "meetings", "people"}

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
    root_docs = [
        ROOT / path.name
        for path in sorted((SRC / "docs").glob("*.md"))
        if path.name not in PLATFORM_DOCS
    ]
    for base in (DIST, PLUGIN / "skills", DOCS, *root_docs):
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

    # 3. onboarding carries the templates it needs to scaffold a workspace,
    # in the plugin and in the drop-in workspace copy alike
    for templates in (
        skills_dir / "onboarding" / "templates",
        DIST / "claude" / "ai-chief-of-staff" / "skills" / "onboarding" / "templates",
    ):
        check(templates.is_dir(), f"onboarding: {templates.relative_to(ROOT)} missing")
        if not templates.is_dir():
            continue
        names = {p.name for p in templates.iterdir()}
        wanted = WORKSPACE_FILES | WORKSPACE_DOCS | {"CLAUDE.md"}
        check(wanted <= names,
              f"{templates.relative_to(ROOT)} missing: {wanted - names}")
        check(OUTPUT_FOLDERS <= names,
              f"{templates.relative_to(ROOT)} missing folders: {OUTPUT_FOLDERS - names}")

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
    for f in WORKSPACE_FILES | WORKSPACE_DOCS | {"CLAUDE.md"}:
        check((ws / f).is_file(), f"claude workspace missing {f}")
    for d in OUTPUT_FOLDERS:
        check((ws / d / "README.md").is_file(), f"claude workspace missing {d}/README.md")
    check({p.name for p in (ws / "skills").iterdir()} == EXPECTED_BEHAVIOURS,
          "claude workspace skills/ incomplete")

    # 6. the ChatGPT pack is complete
    cg = DIST / "chatgpt"
    check((cg / "PROJECT-INSTRUCTIONS.md").is_file(),
          "chatgpt: PROJECT-INSTRUCTIONS.md missing from the top level")
    for f in WORKSPACE_FILES | WORKSPACE_DOCS | {"PROJECT-INSTRUCTIONS.md"}:
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

    # 10. the release zip exists, stands alone, and unzips to one folder.
    # Two zips in dist/ and nothing marking the current one is how a consultant
    # ends up deploying a release that is a version behind.
    release = DIST / f"ai-chief-of-staff-v{version}.zip"
    check(release.is_file(), f"release zip {release.name} missing")
    found_zips = sorted(p.name for p in DIST.glob("ai-chief-of-staff-v*.zip"))
    check(found_zips == [release.name],
          f"dist/ must hold exactly one release zip, the one matching VERSION "
          f"({version}); found {found_zips}")
    if release.is_file():
        with zipfile.ZipFile(release) as zf:
            roots = {e.split("/")[0] for e in zf.namelist()}
        check(roots == {"ai-chief-of-staff"},
              f"release zip should unzip to one folder, got {roots}")

    # 11. the worked example ships in both packs, finished and identical
    fence = re.compile(r"^```.*?^```", re.S | re.M)
    inline = re.compile(r"`[^`\n]*`")
    # a slot starts with a letter, so a real bracketed date reads as a value.
    # the negative lookahead lets a markdown link through.
    slot = re.compile(r"\[[A-Za-z][^\]\n]*\](?!\()")
    for ex in EXAMPLE_ROOTS:
        check(ex.is_dir(), f"example tree missing: {ex.relative_to(ROOT)}")
        if not ex.is_dir():
            continue
        for f in WORKSPACE_FILES | {"README.md"}:
            check((ex / f).is_file(), f"{ex.relative_to(ROOT)}: example missing {f}")
        for d in sorted(EXAMPLE_FOLDERS):
            check((ex / d).is_dir() and any((ex / d).rglob("*.md")),
                  f"{ex.relative_to(ROOT)}: example {d}/ has no worked file in it")
        for path in sorted(ex.rglob("*.md")):
            # fenced and inline code are format specs, not blanks left unfilled
            body = inline.sub("", fence.sub("", path.read_text(encoding="utf-8")))
            slots = slot.findall(body)
            check(not slots,
                  f"{path.relative_to(ROOT)}: unfilled placeholder(s) {sorted(set(slots))[:5]}")
            hits = token.findall(body)
            check(not hits, f"{path.relative_to(ROOT)}: unresolved token(s) {sorted(set(hits))}")

    # the example is copied, never rendered, so the two packs must agree byte
    # for byte. A stray render() pass would show up here as a {{MANUAL}} that
    # resolved two different ways.
    left, right = EXAMPLE_ROOTS
    if left.is_dir() and right.is_dir():
        left_files = {p.relative_to(left) for p in left.rglob("*") if p.is_file()}
        right_files = {p.relative_to(right) for p in right.rglob("*") if p.is_file()}
        check(left_files == right_files,
              f"the two example trees hold different files: {left_files ^ right_files}")
        for rel in sorted(left_files & right_files):
            check((left / rel).read_bytes() == (right / rel).read_bytes(),
                  f"example/{rel}: the packs disagree, it must be copied verbatim")

    # 12. every doc in src/docs/ reached the repo root and the release zip,
    # and the example reached the release zip with them
    entries: set[str] = set()
    if release.is_file():
        with zipfile.ZipFile(release) as zf:
            entries = set(zf.namelist())
    docs = sorted((SRC / "docs").glob("*.md"))
    check(bool(docs), "src/docs/ holds no docs")
    for doc in docs:
        if doc.name in PLATFORM_DOCS:
            # one render per platform, under docs/, and both in the release zip.
            # A doc that splits and then only ships one side is worse than one
            # that never split, because the missing platform looks unsupported.
            for platform in ("claude", "chatgpt"):
                built = DOCS / platform / doc.name
                check(built.is_file(), f"{doc.name}: no {platform} render at docs/{platform}/")
                check(f"ai-chief-of-staff/docs/{platform}/{doc.name}" in entries,
                      f"docs/{platform}/{doc.name}: built but dropped from the release zip")
                if built.is_file():
                    check(built.stat().st_size > 0, f"docs/{platform}/{doc.name} is empty")
        else:
            check((ROOT / doc.name).is_file(), f"{doc.name}: never written to the repo root")
            check(f"ai-chief-of-staff/{doc.name}" in entries,
                  f"{doc.name}: written to the repo root but dropped from the release zip")

    # a split doc that renders identically on both platforms is not split, it is
    # duplicated, and the reader pays for a choice that buys them nothing
    for name in sorted(PLATFORM_DOCS):
        left, right = DOCS / "claude" / name, DOCS / "chatgpt" / name
        if left.is_file() and right.is_file():
            check(left.read_bytes() != right.read_bytes(),
                  f"{name}: the two renders are identical, so it should not be in PLATFORM_DOCS")

    # nothing platform-specific may be left at the repo root, or a reader finds
    # two copies of the same guide and cannot tell which one is current
    for name in sorted(PLATFORM_DOCS):
        check(not (ROOT / name).exists(),
              f"{name}: a stale root copy survives beside docs/, delete it")
    for ex in EXAMPLE_ROOTS:
        prefix = f"ai-chief-of-staff/{ex.relative_to(ROOT).as_posix()}/"
        check(any(e.startswith(prefix) for e in entries),
              f"release zip: nothing under {prefix}")

    # 13. onboarding's step 0 table names every file in src/workspace/.
    # A template can ship in the pack, in onboarding's own templates/ folder,
    # and in the plugin, and still never get created, because the only thing
    # that copies it is a row in that table. decisions.md shipped that way once.
    onboarding = (SRC / "behaviours" / "0-onboarding.md").read_text(encoding="utf-8")
    step_zero = re.search(r"^## Step 0\b.*?(?=^## )", onboarding, re.S | re.M)
    check(bool(step_zero), "0-onboarding.md: no Step 0 section to read the scaffold table from")
    if step_zero:
        # only the table rows count. Prose in the section that happens to name a
        # file is not an instruction to create one.
        table = "\n".join(
            line for line in step_zero.group(0).splitlines() if line.startswith("|")
        )
        check(bool(table), "0-onboarding.md step 0: no scaffold table")
        for path in sorted((SRC / "workspace").glob("*.md")):
            # the manual is named per platform, so it appears as its token
            wanted = "{{MANUAL}}" if path.stem == "_manual" else path.name
            check(wanted in table,
                  f"0-onboarding.md step 0 does not name {wanted}, "
                  "so onboarding will never create it")

    # 14. the "What is in the folder" tree matches the folder that ships.
    # v1.2.0 shipped a ChatGPT tree listing CLAUDE.md, skills/, and example/.
    # A ChatGPT workspace has none of those: the manual is PROJECT-INSTRUCTIONS.md,
    # the behaviours are the prompts you paste, and the example sits beside the
    # workspace. Every one of those files was internally consistent, so nothing
    # structural caught it. Only a client comparing the guide to their own folder
    # would have, which is the worst possible place to find it.
    entry_re = re.compile(r"^(?:\u251c\u2500\u2500|\u2514\u2500\u2500)\s+(\S+)")
    for platform, workspace in WORKSPACE_ROOTS.items():
        guide = DOCS / platform / "READ-ME-FIRST.md"
        if not guide.is_file() or not workspace.is_dir():
            continue
        section = re.search(
            r"^## What is in the folder\b.*?^```\n(.*?)^```",
            guide.read_text(encoding="utf-8"),
            re.S | re.M,
        )
        check(bool(section),
              f"docs/{platform}/READ-ME-FIRST.md: no 'What is in the folder' tree to verify")
        if not section:
            continue
        documented: set[str] = set()
        for line in section.group(1).splitlines():
            found = entry_re.match(line.strip("\n"))
            if found:
                documented.add(found.group(1).rstrip("/"))
        check(bool(documented),
              f"docs/{platform}/READ-ME-FIRST.md: the folder tree parsed to nothing")

        # every documented path has to exist in that platform's shipped workspace
        for name in sorted(documented):
            check((workspace / name).exists(),
                  f"docs/{platform}/READ-ME-FIRST.md names {name}, "
                  f"which is not in {workspace.relative_to(ROOT)}")

        # and the reverse, or a file ships that the leader is never told about.
        # decisions.md shipped undocumented once already, in v1.1.
        shipped = {child.name for child in workspace.iterdir()
                   if not child.name.startswith(".")}
        for name in sorted(shipped - documented):
            check(False,
                  f"{workspace.relative_to(ROOT)} ships {name}, "
                  f"which docs/{platform}/READ-ME-FIRST.md never names")

    # 15. every filename SCHEDULES tells a consultant to paste is one a
    # behaviour actually writes. The prompt text is the whole deployment: a
    # consultant pastes it once and nobody reads it again for a month. If a
    # behaviour renames its output and SCHEDULES keeps the old suffix, the job
    # still runs and still writes a file, and the behaviour downstream that
    # reads it by name finds nothing. Every file in briefs/ carries a suffix so
    # that two jobs on one day never collide and one job can find another's
    # output, and that convention only holds if both sides agree on it.
    declared_briefs: dict[str, set[str]] = {}
    declared_meetings: set[str] = set()
    for path in sorted((SRC / "behaviours").glob("*.md")):
        name = re.sub(r"^\d+-", "", path.stem)
        text = path.read_text(encoding="utf-8")
        declared_briefs[name] = set(re.findall(r"briefs/YYYY-MM-DD-([a-z-]+)\.md", text))
        declared_meetings |= set(
            re.findall(r"meetings/YYYY-MM-DD-\[slug\]/([a-z-]+)\.md", text)
        )
    every_brief_suffix = {s for suffixes in declared_briefs.values() for s in suffixes}
    check(bool(every_brief_suffix), "no behaviour declares a briefs/ output to check against")

    example_re = re.compile(
        r"for example\s+\d{4}-\d{2}-\d{2}-?([A-Za-z0-9/._-]*)\.md", re.S
    )
    for platform in ("claude", "chatgpt"):
        schedules = DOCS / platform / "SCHEDULES.md"
        if not schedules.is_file():
            continue
        for example in sorted(set(example_re.findall(schedules.read_text(encoding="utf-8")))):
            if "/" in example:
                # a meetings folder, so only the filename inside it is the contract
                check(example.rsplit("/", 1)[1] in declared_meetings,
                      f"docs/{platform}/SCHEDULES.md names {example}.md, "
                      "which no behaviour writes into meetings/")
            else:
                check(example in every_brief_suffix,
                      f"docs/{platform}/SCHEDULES.md names a -{example}.md brief, "
                      "which no behaviour writes")

    # and the reverse, on the platform whose prompts save files. A scheduled job
    # whose prompt never names its filename lets two jobs collide on one day,
    # which is the collision the suffixes exist to prevent.
    claude_schedules = DOCS / "claude" / "SCHEDULES.md"
    if claude_schedules.is_file():
        text = claude_schedules.read_text(encoding="utf-8")
        clock = re.search(r"## One clock.*?(?=\n## |\Z)", text, re.S)
        check(bool(clock), "docs/claude/SCHEDULES.md: no clock section to read the scheduled jobs from")
        if clock:
            scheduled = set(re.findall(r"`([a-z-]+)`", clock.group(0))) & set(declared_briefs)
            check(bool(scheduled), "docs/claude/SCHEDULES.md: the clock names no known behaviour")
            for job in sorted(scheduled):
                for suffix in sorted(declared_briefs[job]):
                    check(f"-{suffix}.md" in text,
                          f"{job} writes briefs/YYYY-MM-DD-{suffix}.md and "
                          "docs/claude/SCHEDULES.md never names that filename")

    if failures:
        print(f"FAILED {len(failures)} of {checks} checks:\n")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print(f"All {checks} checks passed.")


if __name__ == "__main__":
    main()
