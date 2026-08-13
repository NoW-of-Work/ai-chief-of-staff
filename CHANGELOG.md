# Changelog

## v1.2.1

Documentation only. No behaviour, workspace file, or approval gate changed.

- **The folder home is now ranked rather than listed.** `READ-ME-FIRST.md` Path A step 2 gave three arrangements as peers and then named two of them "safest" in a closing sentence. It now gives three homes in order, each with the one thing it gives up: files saved to the Claude account give up the leader's own filesystem, a connector source gives up certainty about appends, and a local folder connected in Cowork gives up unattended runs. Every home fails something, and saying which is the decision the consultant is actually making.
- **One vocabulary per platform.** `DEPLOY-FOR-A-CLIENT.md` said "cloud storage the leader owns" on both platforms. On ChatGPT that is exactly right. On Claude it points at a connector source, which is the one home whose appends are not documented, so the runbook was steering Claude deployments toward the weakest option while `READ-ME-FIRST.md` steered them away. The phrase is now ChatGPT-only, and the Claude block names the three homes instead.
- **The two docs no longer contradict each other about laptops.** `DEPLOY-FOR-A-CLIENT.md` preferred "a folder connected in Cowork" while its own table, its troubleshooting section, and `SCHEDULES.md` all ruled a laptop out. A local folder is now a documented option 3 with a stated cost, and all four places say the same thing in the same words.
- **The append test is mandatory, whichever home you chose.** It was asked for only when Drive was the fallback, which is the case a consultant already distrusts. The home nobody thinks to doubt is the one that reads fine and silently writes nothing.
- **Path A distinguishes Cowork from Claude Code.** It read "Claude Code or Claude Cowork" as if a terminal and a desktop app were interchangeable for a non-technical leader. Cowork is the default and carries the connector toggles and the scheduled-tasks panel; Claude Code is for a leader who is technical and asks for it. `README.md` routes the same way.
- **The ChatGPT folder map matched no ChatGPT deployment.** "What is in the folder" listed `CLAUDE.md`, `skills/`, and `example/`. A ChatGPT workspace ships `PROJECT-INSTRUCTIONS.md`, has no `skills/` because the behaviours are the prompts you paste, and keeps `example/` beside the workspace rather than inside it. The tree is now split per platform and each one lists what that platform actually ships.
- **Two more hardcoded manual names became `CLAUDE.md`.** The "if you only change one thing" line and the `SCHEDULES.md` note on naming the manual both said `CLAUDE.md` in the ChatGPT render. Split docs exist so a reader never meets the other platform's paths, and these were the last two that leaked.

## v1.2.0

- The install guide, the schedule prompts, and the client runbook now render once per platform, into `docs/claude/` and `docs/chatgpt/`. A consultant deploys to one platform and reads only the paths that apply to it. A Claude deployment reads 836 lines where the combined set was 1,099, and a ChatGPT deployment 864. `SCHEDULES.md` alone goes from 557 lines to 345 and 376.
- Filenames are identical in both directories, so every cross-link between docs resolves inside whichever set the reader opened and no link has to know its own platform.
- `README.md` is the router. It names the two sets and says to read only one.
- Every cross-platform path reference removed. A Claude reader is no longer sent to a Path C their guide does not contain, and a ChatGPT reader no longer reads three bullets about what Path A leaves out.
- `QUICK-START.md`, `CHANGELOG.md`, and `CREDITS.md` stay single at the repo root. The leader's page reads the same on both platforms, and splitting it would double a file to vary one sentence.
- `build.py` gains `PLATFORM_DOCS`. Anything named there renders once per platform into `docs/`; everything else renders once to the root.
- `check.py` gains three rules, 465 checks to 486: both renders of a split doc exist and reach the release zip, the two renders differ (a doc that splits identically is duplicated rather than split), and no stale root copy survives beside `docs/`.

## v1.1.0

- Five new behaviours: `inbox-triage`, `chase`, `decision-brief`, `recall`, `health-check`. Thirteen in total.
- New workspace file `decisions.md`: closed calls, the reasoning, the conditions that would reopen each one, and a Monday review pass over the ones that have come due.
- Three new approval gates, thirteen in total. No outcome written to `decisions.md` that the leader has not stated in the same session, no state changed in a connected source, and `tomorrow.md` never saved without approval.
- New `example/` folder: a filled-in workspace for an invented leader, plus one brief, one person file, and one meeting note. Reference only. No behaviour reads it.
- New `QUICK-START.md` for the leader, `DEPLOY-FOR-A-CLIENT.md` for whoever installs it, and `SCHEDULES.md` with every recurring prompt in full.
- `READ-ME-FIRST.md` corrected against current platform documentation: plugin install differs between Claude Code and Claude Cowork and does not run in ordinary Claude chat, skill uploads need **Code execution and file creation** on first and live under **Customize > Skills**, ChatGPT can write files through a connected app, ChatGPT caps active scheduled tasks per plan and cannot run one more often than hourly, and a cloud scheduled run reaches connected sources rather than a hard drive.
- `READ-ME-FIRST.md` now points at `SCHEDULES.md` for prompt text rather than restating it.
- The eight original behaviours updated to carry their half of the new contracts. `onboarding` creates `decisions.md` and hands off to `health-check`. `weekly-review` renders the Monday decisions pass and leaves the chase drafts to `chase`. `morning-brief` renders what the morning triage pass appended and drafted, and reads it once. `end-of-day-close` runs a triage pass when none has run since morning.
- Every file in `briefs/` now carries a suffix, including the morning brief (`YYYY-MM-DD-brief.md`), so two jobs on one day never collide and a behaviour reading another's output can find it by name.
- `chase` runs two or three days after `weekly-review` rather than the same morning, and reads that week's review so a release is proposed once.
- Build copies `src/example/` into the workspace and `decisions.md` into the workspace templates. `check.py` now fails when `onboarding` step 0 does not name every file in `src/workspace/`.

## v1.0.0

First public release.

- Eight behaviours: `onboarding`, `morning-brief`, `meeting-prep`, `transcript-to-actions`, `daily-transcript-sweep`, `end-of-day-close`, `weekly-review`, `connection-check`.
- Six workspace files and four output folders, created automatically by `onboarding` when they do not exist.
- Capability registry (`connections.md`) tracking Calendar, Email, Documents, Transcripts, Chat, Tasks, and CRM by job rather than by vendor.
- Three-gate nudge policy, one capability line per brief maximum, permanent silencing on request.
- Ten approval gates. The system drafts and never sends.
- Single-source build producing the Claude plugin, the Claude drop-in folder, per-behaviour upload ZIPs, and the ChatGPT project pack.
