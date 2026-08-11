# AI Chief of Staff

**v{{VERSION}} · Created by [The NoW of Work](https://www.nowofwork.com) · MIT licensed**

An AI chief of staff for one leader. Morning briefs, prep before the meetings that matter, action items out of recorded calls, inbox triage, a ledger of open promises, a record of closed decisions, and a Monday review. Built out of plain text files the leader owns.

Runs on Claude and on ChatGPT. Both versions are generated from one source, so they cannot drift apart.

### → **[READ ME FIRST](READ-ME-FIRST.md)** is the install guide. Start there.

---

## The short version

```
/plugin marketplace add NoW-of-Work/ai-chief-of-staff
/plugin install ai-chief-of-staff@now-of-work
```

Then say **"run onboarding"** and answer six questions. Everything else is inferred from the calendar and mail the leader already has.

Those two lines are Claude Code. In Claude Cowork, add the marketplace through **Customize > Plugins**. Not using plugins, or using ChatGPT? Download the repo as a ZIP, unzip once, and follow [READ-ME-FIRST.md](READ-ME-FIRST.md).

---

## What it does

Thirteen behaviours. Nine of them can run on a schedule.

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
| `inbox-triage` | Twice a working day | Mail cut to what needs a person: decisions waiting, drafted replies, promises both ways, a count of what it left alone |
| `chase` | Weekly | What the leader is owed and has not been given, a release call on what died, and at most three drafts sized to the relationship |
| `decision-brief` | When a decision is due, plus a Monday pass | The choice, the options and their costs, the leader's own filters, a recommendation with two falsifiers |
| `recall` | On demand | An answer out of the leader's own record, the file it came from, conflicts between sources, and what was searched and not found |
| `health-check` | Monthly | Whether the workspace is actually configured: blocking gaps, stale files, contradictions, folders that are not filling, one verdict |

---

## The three ideas it is built on

**It drafts, it does not act.** No sending, no booking, no replying. Twelve approval gates, listed in the operating manual, and none of them are negotiable.

**It knows what it cannot see.** A registry file tracks capabilities (Calendar, Email, Documents, Transcripts, Chat, Tasks, CRM) rather than vendors. That is the only reason the system can tell "nothing happened yesterday" apart from "I cannot see what happened yesterday." Those look the same in the output and they are completely different problems.

**It stays quiet.** A missing tool earns at most one line, at most once a fortnight, and only on a day where that tool would actually have paid for itself. Say "not now" twice and it never asks again. Three weeks out of four it says nothing at all about itself.

---

## Repository layout

| Path | What it is |
|------|-----------|
| `READ-ME-FIRST.md` | The install guide |
| `QUICK-START.md` | The page you hand the leader once it is installed |
| `DEPLOY-FOR-A-CLIENT.md` | The runbook for installing it for somebody else |
| `SCHEDULES.md` | Every recurring job as copy-paste prompt text, in the order to add them |
| `src/` | **The only thing you edit.** Behaviours, workspace templates, the worked example, docs |
| `build/build.py` | Generates every output below from `src/` |
| `plugin/` | The Claude plugin. `skills/` inside it is generated |
| `dist/claude/` | Drop-in workspace folder, plus one upload ZIP per behaviour |
| `dist/chatgpt/` | Project instructions, thirteen prompt files, workspace files |
| `.claude-plugin/marketplace.json` | Lets anyone install this with `/plugin marketplace add` |

Everything under `dist/` and `plugin/skills/` is generated and committed, so a client can download and use the repo without running anything. Every markdown file in the repo root is generated too, this README included. Edit the copy in `src/docs/` and let the build write the root one.

### Inside `src/`

| Path | What it is |
|------|-----------|
| `src/behaviours/` | Thirteen behaviour files, one per skill. YAML frontmatter carries `name`, `order`, and a description under 200 characters |
| `src/workspace/` | The seven files that make up a workspace: `_manual.md`, `about-me.md`, `my-work.md`, `tomorrow.md`, `commitments.md`, `decisions.md`, and `connections.md`, plus a README per output folder |
| `src/example/` | A filled-in workspace for a leader who does not exist. Copied into every build so the leader has something to compare against |
| `src/docs/` | Every markdown file that lands in the repo root. Rendered with `platform=claude`, so ChatGPT specifics go in as plain prose |

`decisions.md` is the leader's record of calls they closed, and the system may open and re-status an entry without writing an outcome the leader has not stated. `src/example/` is reference only. No behaviour reads it, and the build copies it in whole.

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
- copies `src/example/` into the built workspace untouched, so the worked example ships beside the empty files
- renders `src/docs/` to the repo root
- checks every skill description against the 200-character limit and fails the build if one is over
- keeps `VERSION`, `plugin.json`, and `marketplace.json` in step
- writes a single release ZIP

Then run `python3 build/check.py`. It verifies the generated output: no unresolved tokens, frontmatter and description limits, matching heading sets across the two platform renders of a behaviour, manifest versions in step with `VERSION`, a release ZIP that unzips to one folder, and a step 0 table in `onboarding` that names every file in `src/workspace/`. That last one exists because a template can ship in all three places and still never get created, since the only thing that copies it is a row in that table.

Bump `VERSION` before you publish. Users only get plugin updates when the version changes.

---

## Credits and permission

Created by **The NoW of Work**.

MIT licensed. You may use it, edit it, adapt it for a client, rebrand it, and ship it commercially. Keep the licence file and the credit line. See [CREDITS.md](CREDITS.md).

*The Future is NoW.*
