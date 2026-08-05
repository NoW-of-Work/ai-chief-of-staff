# AI Chief of Staff

**v{{VERSION}} · Created by [The NoW of Work](https://www.nowofwork.com) · MIT licensed**

An AI chief of staff for one leader. Morning briefs, prep before the meetings that matter, action items out of recorded calls, a ledger of open promises, and a Monday review. Built out of plain text files the leader owns.

Runs on Claude and on ChatGPT. Both versions are generated from one source, so they cannot drift apart.

### → **[READ ME FIRST](READ-ME-FIRST.md)** is the install guide. Start there.

---

## The short version

```
/plugin marketplace add nowofwork/ai-chief-of-staff
/plugin install ai-chief-of-staff@now-of-work
```

Then say **"run onboarding"** and answer six questions. Everything else is inferred from the calendar and mail the leader already has.

Not using plugins, or using ChatGPT? Download the repo as a ZIP, unzip once, and follow [READ-ME-FIRST.md](READ-ME-FIRST.md).

---

## What it does

| Behaviour | When | What comes out |
|-----------|------|----------------|
| `onboarding` | Once, at setup | A filled-in workspace, built from the calendar and mail rather than a questionnaire |
| `morning-brief` | Every morning | Under 400 words: today's priorities, the meetings that need something, open loops, drafts waiting on a yes |
| `meeting-prep` | Before a meeting that matters | Who, why, what happened last time, what is open between you both ways, three questions, the risks |
| `transcript-to-actions` | After a recorded call | Decisions, action items with owners, commitments for the ledger, what was too ambiguous to call |
| `daily-transcript-sweep` | Daily | Yesterday's meetings turned into actions without being asked |
| `end-of-day-close` | End of day | What moved, what came in, and a draft of tomorrow for the leader to approve |
| `weekly-review` | Monday | What slipped, where the time actually went, drift against what they said they are not doing |
| `connection-check` | Weekly | Notices tools that appeared, tools that quietly broke, and decides (rarely) whether a gap is worth one line |

---

## The three ideas it is built on

**It drafts, it does not act.** No sending, no booking, no replying. Ten approval gates, listed in the operating manual, and none of them are negotiable.

**It knows what it cannot see.** A registry file tracks capabilities (Calendar, Email, Documents, Transcripts, Chat, Tasks, CRM) rather than vendors. That is the only reason the system can tell "nothing happened yesterday" apart from "I cannot see what happened yesterday." Those look the same in the output and they are completely different problems.

**It stays quiet.** A missing tool earns at most one line, at most once a fortnight, and only on a day where that tool would actually have paid for itself. Say "not now" twice and it never asks again. Three weeks out of four it says nothing at all about itself.

---

## Repository layout

| Path | What it is |
|------|-----------|
| `READ-ME-FIRST.md` | The install guide |
| `src/` | **The only thing you edit.** Behaviours, workspace templates, docs |
| `build/build.py` | Generates every output below from `src/` |
| `plugin/` | The Claude plugin. `skills/` inside it is generated |
| `dist/claude/` | Drop-in workspace folder, plus one upload ZIP per behaviour |
| `dist/chatgpt/` | Project instructions, eight prompt files, workspace files |
| `.claude-plugin/marketplace.json` | Lets anyone install this with `/plugin marketplace add` |

Everything under `dist/` and `plugin/skills/` is generated and committed, so a client can download and use the repo without running anything.

---

## Maintaining a fork

Edit `src/`, then:

```bash
python3 build/build.py     # or: make build
```

One source, every output. The build:

- turns each behaviour in `src/behaviours/` into a Claude skill and a ChatGPT prompt
- resolves `{{#claude}}` and `{{#chatgpt}}` blocks so each version says the right thing about its own platform
- copies the workspace templates into the `onboarding` skill, so setup can create files that do not exist yet
- checks every skill description against the 200-character limit and fails the build if one is over
- keeps `VERSION`, `plugin.json`, and `marketplace.json` in step
- writes a single release ZIP

Bump `VERSION` before you publish. Users only get plugin updates when the version changes.

---

## Credits and permission

Created by **The NoW of Work**.

MIT licensed. You may use it, edit it, adapt it for a client, rebrand it, and ship it commercially. Keep the licence file and the credit line. See [CREDITS.md](CREDITS.md).

*The Future is NoW.*
