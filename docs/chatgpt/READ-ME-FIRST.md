# READ ME FIRST

**AI Chief of Staff, v1.3.0. Created by The NoW of Work.**

This is the whole setup guide. If you read one file, read this one.

---

## What you are installing

An AI chief of staff for one leader. It reads your calendar, mail, documents, and meeting notes, and it produces a short morning brief, prep before meetings that matter, action items out of recorded calls, a ledger of open promises, a record of closed decisions, and a Monday review.

It works from plain text files. Five belong to you, one belongs to the system, and every one of them opens in any editor. There is no database, no account to create, and nothing that runs outside the AI tool you already pay for.

**It drafts. It does not send.** No email, no calendar changes, no replies. Everything that touches another person goes through you first.

### The other files you will want

| File | Open it when |
|------|--------------|
| `QUICK-START.md` | You want the ten-minute version, or you are handing this to someone else to use. It is the same system said shorter |
| `SCHEDULES.md` | You are setting up recurring jobs. Every prompt in full, the order to add them in, and a worked weekly clock |
| `example/` | You want to know what this is supposed to look like. An invented leader at an invented company, every file answered the way a real one would answer it, plus one brief, one person file, and one meeting note. It ships with the download. In the Claude pack it sits inside the workspace folder. In the ChatGPT pack it sits beside `workspace/`, on disk, and it is never uploaded to the project. Nothing reads it either way. It is there to compare against |

---

## Before you start

Three things, and only the first one is required.

| | What | Why |
|---|------|-----|

| 1 | A paid ChatGPT account (Go, Plus, Edu, Pro, Business, or Enterprise) | The system runs inside it, and a free account cannot hold the files or run the schedules. The plan is also a ceiling on the ramp, because each one caps how many scheduled tasks can be active at once: 3 on Go, 5 on Plus, 10 on Business and Edu, 15 on Pro and Enterprise. The finished clock is ten tasks, so Business, Edu, Pro, and Enterprise carry all of it, Plus carries five, and Go stalls in week two. Settle this before you plan the ramp rather than when a task refuses to save |

| 2 | A calendar connected to it | Almost everything is built on the calendar |
| 3 | Email connected to it | Open loops, follow-ups, and voice all come from mail |

Anything else (documents, transcripts, chat, tasks, CRM) is optional. The system notices what is missing, works around it, and offers to use new tools when they appear. You do not have to connect everything on day one, and you probably should not.

**One thing worth knowing before you start.** Setup reads about twenty of your own sent emails to learn how you write, and four weeks of your calendar to learn your working rhythm. It reads them; it does not store them. If you would rather it did not read your mail at all, setup still works: you write three bullets about your own voice instead, and the drafts are slightly less like you until you correct a few.

If somebody else manages your calendar or your inbox, tell them before you run this. The system will start commenting on how your week is built, and that is their work you are grading.

---

## Install: pick one path

This is the ChatGPT copy of the guide, so it carries one path and it is below. If you are on Claude, read `docs/claude/READ-ME-FIRST.md` instead, which has two.

---

## Path C: ChatGPT

**Step 1.** Download this repository as a ZIP and unzip it once. Everything you need is in `dist/chatgpt/`.

**Step 2.** Create a new ChatGPT Project called **AI Chief of Staff**.

**Step 3.** Open `dist/chatgpt/PROJECT-INSTRUCTIONS.md`, copy all of it, and paste it into the project's custom instructions.

**Step 4.** Upload these to the project's files:

- seven of the eight files sitting at the top of `dist/chatgpt/workspace/`: `PROJECT-INSTRUCTIONS.md`, `about-me.md`, `my-work.md`, `tomorrow.md`, `commitments.md`, `decisions.md`, `connections.md`
- all fourteen files in `dist/chatgpt/prompts/`

The eighth file at the top of `workspace/` is `QUICK-START.md`, and it stays on disk. It is the ten-minute version, and the page to hand anyone else who will be using this. No prompt or instruction file reads it, so uploading it spends a project file slot on something the system never opens.

`workspace/` also holds `archive/`, `briefs/`, `meetings/`, and `people/`, each with a `README.md` stub inside it. Leave all four alone. A ChatGPT project is a flat list of files with no folders to stub, so the stubs do no work there, and uploading them makes it twenty-four files instead of twenty.

Do not upload `dist/chatgpt/example/`. It is reference for you, not input for the system, and no prompt or instruction file points at it. Leave it in the unzipped folder on disk and open it there when you want to see what a filled-in file looks like.

That is twenty files before the system has written a single brief. Projects cap the file count per plan: 5 on Free, 25 on Go and Plus, 40 on Edu, Pro, Business, and Enterprise. Free cannot hold the twenty at all. Go and Plus leave five slots for everything the system produces afterwards, so archive briefs monthly on those two. The other plans leave twenty. Upload the four stubs by mistake and Plus is down to one free slot.

**Step 5.** Put the workspace where a scheduled run can reach it. Copy those same seven files into a folder called `ai-chief-of-staff` in Google Drive, or in another app connected to ChatGPT.

This is not a duplicate for its own sake. A scheduled task cannot read a project's files, including the files of the project it was created in, so the 07:00 run reads the connected folder or it reads nothing. The project upload still earns its keep for the sessions you open yourself, where project files are readable and retrieval is better.

Two copies means keeping two copies in step, which is ongoing friction worth knowing about before you commit to this platform. A scheduled run prints its output for you to paste rather than writing it back, because a write needs an approval and nobody is there to give one, so paste into the connected folder first and bring the project copy along when you get to it. `SCHEDULES.md` carries every prompt that depends on this and names the folder in the first line of each one.

If you will not connect an app, say so plainly rather than scheduling anyway: ChatGPT cannot run this unattended. The fallback is a trigger-only task that says "it is 07:00, run the morning brief," with you running the real prompt inside the project by hand.

**Step 6.** Go to **Run onboarding**, below.

### What is different in ChatGPT

The behaviours, the approval gates, the voice rules, and the nudge policy are identical, because both versions are generated from the same source. Four differences remain.

**Writing files.** Claude writes into a connected folder or workspace directly. ChatGPT writes through a connected app, most often Google Drive, and asks for approval before each write. Whether it can write at all depends on the plan and, in a managed workspace, on what an admin has enabled. Where nothing is connected, it prints the output in a code block and you save it. A response can also be kept with **Save to project** from the message menu.

**Knowing what it can reach.** ChatGPT cannot see which connectors it has, so setup asks you which tools are connected and then verifies by trying each one. What it can reach also varies by plan, workspace, and admin settings, and it can change between one session and the next. Treat the answer as a snapshot and let the weekly connection check refresh it.

**Scheduled runs and project files.** A ChatGPT scheduled task cannot read the files attached to a project, including the project it was created in. The workspace has to live in a connected app for a scheduled run to reach it, which is what Path C step 5 sets up. That leaves two copies: the connected folder the schedule reads, and the project upload that serves the sessions you open. Connected apps do survive into a scheduled run, so the run can still reach mail and calendar. Claude Cowork has the same shape of limit for a different reason: a cloud run reaches connectors, and the hard drive is out of reach.

**Packaging.** Claude has a plugin that installs all fourteen behaviours in one step, in Claude Code and Claude Cowork. ChatGPT installs as a project: paste the instructions, upload the files. Two things that used to differ no longer do. ChatGPT can write files, and it can run recurring work on a schedule. Neither platform will send anything on your behalf without approval, and this system never asks either of them to.

---

## Run onboarding

This is the actual setup. Ten minutes, most of it you reading a list and saying "that one's wrong."

Start a session and say:

> **Run onboarding.**

Point it at the folder if it asks. It will:

1. **Create any missing files.** You never have to make one by hand.
2. **Check what it can reach** and write that down.
3. **Draft your profile** from the calendar, sent mail, and documents. Everything it guessed is labelled `(inferred)`.
4. **Show you what it worked out** in one scannable block and ask what to fix.
5. **Ask six questions**, and only six. They are the things no tool can ever reveal.
6. **Save**, once you approve.

**The corrections are the product.** Every "no, it's actually X" turns a guess into a fact. Do not rush this to get to the brief.

### Then spend twenty more minutes on four answers

Anything still in `[BRACKETS]` after onboarding is a decision nobody has made yet. That is allowed. Four of them do more work than everything else combined: `about-me.md` section 6 (who you can never miss), `about-me.md` section 8 (hard stops), `my-work.md` section 1 (what this quarter is actually for), and `my-work.md` section 5 (what they are not doing).

Spend longest on the last one. A system that knows what you are avoiding is more useful than one that only knows what you want.

The honest answer is harder to write than it looks, because the polite version arrives first. "We are not prioritising international expansion" is a press release. "Rocky keeps pulling me into partner calls I add nothing to" is the thing a Monday review can actually catch you drifting back into. Write the second kind.

---

## Run the first brief

> **Run the morning brief.**

What good looks like: under 400 words. Starts with the work, not a greeting. Two to four priorities with a reason each. Only the meetings that need something. Every claim traceable to a file or a source, and anything uncertain labelled. `example/briefs/` holds one that hits the mark, if you want something to hold it against. In ChatGPT that folder is not in the project. It is at `dist/chatgpt/example/briefs/` in the unzipped folder on disk, so open it there.

**There should be nothing about connections on day one.** That is correct. The system just set its own timers, so it has nothing to say yet. An empty capability section on the first brief means it is working.

---

## Schedule it

Add **the morning brief only**. Nothing else this week.

`SCHEDULES.md` carries the exact prompt text for every recurring job, on both platforms, plus the week-by-week order to add them in and a worked clock. Copy from there rather than writing your own. Nine of the fourteen behaviours can run on a schedule, across ten tasks, because inbox triage runs twice a day.

**In ChatGPT.** Open **Scheduled** in the sidebar and choose **New task**. Four limits shape the plan. A task cannot run more often than hourly. Each plan caps how many can be active at once: 3 on Go, 5 on Plus, 10 on Business and Edu, 15 on Pro and Enterprise, so the ten-task clock needs Business, Edu, Pro, or Enterprise, and Plus tops out at five jobs. A task pauses itself if it sits unused, or if the chat it belongs to is deleted. And it reads the connected folder from Path C step 5, never the project's files, so the prompt has to name that folder.

Two things catch people out:

- **Most scheduled runs start fresh.** They remember nothing from your conversations, so the prompt has to name the folder every time. ChatGPT monitoring tasks are the exception. They remember earlier runs so they can report only what changed.
- **A scheduled run in the cloud reaches connected sources.** Your hard drive is out of reach. See Path C step 5 on where the folder has to live.

**Do not add the whole ramp on day one.** Nine outputs nobody opens is worse than one that gets read. The transcript sweep exits silently every day until a transcription tool is connected, which is designed rather than broken.

---

## Run it for a week before changing anything

The first week's corrections are the real setup. When it gets a name wrong, mishears a priority, or drafts in the wrong tone, fix the source file rather than the output. That is what makes week two better.

---

## What is in the folder

```
ai-chief-of-staff/
├── PROJECT-INSTRUCTIONS.md  The operating manual. Read first on every run.
├── QUICK-START.md           The ten-minute version. Nothing reads it.
├── connections.md           What the system can reach. It maintains this itself.
├── about-me.md              Who you are, how you work, your voice.
├── my-work.md               What is active right now, and what is not.
├── tomorrow.md              The leader's intent for the next working day.
├── commitments.md           Open promises, both directions.
├── decisions.md             Calls you closed, and what would reopen each one.
├── briefs/                  Output. Briefs, closes, reviews, drafts.
├── meetings/                Output. One folder per meeting.
├── people/                  Output. One file per person who matters.
└── archive/                 Output. Closed commitments, resolved loops.
```

Five files you own. One file the system owns. Four folders that fill themselves.

The behaviours are not in this folder on ChatGPT. They are the prompts in `prompts/`, which you paste. The worked example sits beside the workspace in `example/`, not inside it, so nothing reads it by accident.

That tree is what the workspace holds once `onboarding` has run. On ChatGPT it lives in the connected folder from Path C step 5, and the project carries a second copy of the same files for the sessions you open. `skills/` has no equivalent, because the behaviours are the thirteen prompt files uploaded to the project rather than files in the workspace.

### Three things worth understanding

**`connections.md` is not yours to fill.** Every other file is written by you and read by the system. This one is the reverse. It exists so the system can tell the difference between "no meetings had transcripts yesterday" and "there is no transcription tool connected." Those look identical in the output and they are completely different problems. It tracks capabilities rather than vendors. "Transcripts" is a row, and Otter, Fathom, Fireflies, Granola, and Grain are things that can fill it. Swap the tool, change one cell, and nothing else needs editing.

**`decisions.md` is a record, not a plan.** The system drafts an entry after you close a call, and it never writes an outcome you have not said out loud in that session. Once an entry reads `Made`, the reasoning in it is never edited, including where it turned out to be wrong. The field that earns the file its keep is **Would change my mind**, because the Monday review pass is the only thing in the system that checks whether a July decision still matches September's facts.

**Nudges are rare on purpose.** When a tool is missing, the system can mention it. Three gates have to pass first: enough time since the last mention, you have not said stop, and something happened that day where the missing tool would actually have helped. That third gate is the one that matters. Being overdue is not a reason to speak. Most mornings there is nothing, and the section does not appear at all.

The exception is a fault. If a connected tool quietly stops working, that gets flagged immediately, every time. A missing tool is a gap you know about. A broken one is a gap they do not.

---

## Adding a tool later

Connect it. Do nothing else.

The next connection check notices, and the next morning brief says one line:

> You connected Fathom. Want me to start the daily sweep, so tomorrow's meetings come back as action items?

Say yes and the behaviour turns on. Say no and it does not come up again. The system will not switch anything on by itself, because a tool appearing in an account is not the same as you asking for a behaviour.

---

## If something goes wrong

**Start by saying "Check the setup."** That runs `health-check`. It reads every file, tests what it can reach, and returns one verdict plus a ranked list: blocking gaps, stale files, contradictions between files, output folders that are not filling. It diagnoses most of the table below on its own, and it edits nothing.

| What you see | What it usually is |
|--------------|-------------------|
| The brief runs long, or opens with "Good morning!" | The operating manual is not being read. Check it is in the project instructions and the session is inside the project. |
| Priorities are generic | `my-work.md` section 2 is still bracketed. Fill it in. |
| It can read files but cannot save them | Write access is not enabled for the storage connector. |
| "(not connected)" about the calendar | The connector dropped or the token expired. Reconnect it. |

| A scheduled task produces nothing useful, or the brief reads generic with none of your context in it | The prompt points at the project rather than the connected folder, so the run reached no files at all. Path C step 5. |

| A ChatGPT scheduled task stopped arriving | It paused itself, or the chat it belonged to was deleted. Open the **Scheduled** page. |
| It invents a meeting detail | Serious. Note the exact line and open an issue. That is a defect, not a setting. |
| It offers to connect something for you | Same. It is never allowed to authenticate anything. |

---

## Making it yours

You are meant to edit this. See `CREDITS.md` for the terms, which are short and permissive.

If you only change one thing, change `PROJECT-INSTRUCTIONS.md` section 6 so the voice rules match the house style of whoever is using it.

If you are going to maintain your own version, edit the files in `src/` and run `python3 build/build.py`. That regenerates the Claude and ChatGPT versions together, so they never drift apart. See `README.md` for how the build works.

---

*Created by The NoW of Work. MIT licensed. Yours to edit, adapt, and rename.*
