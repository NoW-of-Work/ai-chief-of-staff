# READ ME FIRST

**AI Chief of Staff, v1.2.1. Created by The NoW of Work.**

This is the whole setup guide. If you read one file, read this one.

---

## What you are installing

An AI chief of staff for one leader. It reads the leader's calendar, mail, documents, and meeting notes, and it produces a short morning brief, prep before meetings that matter, action items out of recorded calls, a ledger of open promises, a record of closed decisions, and a Monday review.

It works from plain text files. Five belong to the leader, one belongs to the system, and every one of them opens in any editor. There is no database, no account to create, and nothing that runs outside the AI tool you already pay for.

**It drafts. It does not send.** No email, no calendar changes, no replies. Everything that touches another person goes through the leader first.

### The other files you will want

| File | Open it when |
|------|--------------|
| `QUICK-START.md` | You are handing the system over. Hand the leader that page and keep this one. Ten minutes, written for them |
| `DEPLOY-FOR-A-CLIENT.md` | You are installing for somebody else. The consent script, a sixty-minute agenda, the four questions, and what to check at day 1, 7, and 30 |
| `SCHEDULES.md` | You are setting up recurring jobs. Every prompt in full, the order to add them in, and a worked weekly clock |
| `example/` | You want to know what this is supposed to look like. An invented leader at an invented company, every file answered the way a real one would answer it, plus one brief, one person file, and one meeting note. It ships with the download. In the Claude pack it sits inside the workspace folder. In the ChatGPT pack it sits beside `workspace/`, on disk, and it is never uploaded to the project. Nothing reads it either way. It is there to compare against |

---

## Before you start

Three things, and only the first one is required.

| | What | Why |
|---|------|-----|

| 1 | A paid Claude account | The system runs inside it. Claude puts no cap on how many scheduled tasks can be active, so the full ten-task clock is available on any paid plan |

| 2 | A calendar connected to it | Almost everything is built on the calendar |
| 3 | Email connected to it | Open loops, follow-ups, and voice all come from mail |

Anything else (documents, transcripts, chat, tasks, CRM) is optional. The system notices what is missing, works around it, and offers to use new tools when they appear. You do not have to connect everything on day one, and you probably should not.

**One thing worth saying out loud before you start.** Setup reads about twenty of the leader's own sent emails to learn how they write, and four weeks of their calendar to learn their working rhythm. That is somebody's real mailbox. Tell them what it reads before it reads it. If they would rather it did not, setup still works, and they write three bullets about their own voice instead.

---

## Install: pick one path

This is the Claude copy of the guide, so it carries the two Claude paths. Pick the first one that describes you. If the leader is on ChatGPT, read `docs/chatgpt/READ-ME-FIRST.md` instead.

- **Path A — Claude, one command.** Fastest. Use this if the leader works in Claude Cowork, which is where almost every leader should be: it carries the connector toggles and the scheduled-tasks panel this system runs on. The same two commands work in Claude Code, but Claude Code is a terminal. Use it only when the leader is technical and asks for it.
- **Path B — Claude, one unzip.** Use this if you would rather not use plugins, or the leader lives in ordinary Claude chat, where plugins do not run.

---

## Path A: Claude, one command

**Step 1.** Install the plugin. **In Claude Code**, run these two lines:

```
/plugin marketplace add NoW-of-Work/ai-chief-of-staff
/plugin install ai-chief-of-staff@now-of-work
```

**In Claude Cowork**, do the same thing through the interface. Open **Customize** in the sidebar, then **Plugins**, then **Add marketplace**, and paste the repository URL. The plugin appears alongside the others, and **Install** puts it in. Plugins run in Claude Code and Claude Cowork. They do not run in ordinary Claude chat, so if the leader lives there, use Path B.

That installs all fourteen behaviours at once. If the install summary says `Run /reload-plugins to activate.`, run it. If the reload warns that it will re-read the conversation, run it again as `/reload-plugins --force`. They arrive as skills, named after the plugin: `/ai-chief-of-staff:onboarding`, `/ai-chief-of-staff:morning-brief`, and so on. You can also just ask for them in plain language, which is what most people do.

> The repository URL, for the Cowork interface and for Path B, is `https://github.com/NoW-of-Work/ai-chief-of-staff`.

**Step 2.** Decide where the workspace lives. This decides whether the system runs unattended, and it is far easier to settle now than to move later.

A scheduled run in the cloud reaches connected apps and the files saved to your Claude account. It does not reach your hard drive, and a folder that syncs to the cloud from a laptop is still your hard drive.

Three homes work, and every one of them gives something up. Pick by which loss you can live with. They are in order.

1. **Files saved to the Claude account.** A cloud run reaches it and appending to a file is documented. What you give up: the working files live in Claude's storage rather than somewhere the leader opens in Finder. This is the default. Choose it unless the leader objects to that.

2. **A source reached through a connector**, such as Google Drive or SharePoint. A cloud run reaches it. What you give up: certainty about appends. Claude's Drive connector documents uploading files, creating folders, reading, and saving files Claude generated. Editing an existing plain markdown file in place is not something it commits to, and this system appends constantly.

3. **A local folder connected in Cowork.** Appends are ordinary file writes, so they are certain, and the leader keeps the files. What you give up: unattended runs. The machine has to be awake and Cowork open at 06:30, and a laptop that dies takes the workspace with it unless it is backed up or in version control. Choose this only when the leader will not put working files in Claude's storage.

**Then test it, whichever one you chose.** Ask the system to append one line to `commitments.md`, then reopen the file and confirm the line is there. Sixty seconds, and it is the only way to catch a home that reads fine and writes nothing. Do this before you schedule anything.

Call the folder `ai-chief-of-staff`. It can be empty. The next step fills it.

**Step 3.** Go to **Run onboarding**, below.

---

## Path B: Claude, one unzip

**Step 1.** Download this repository as a ZIP (the green **Code** button at the top of the GitHub page, then **Download ZIP**) and unzip it once.

**Step 2.** Inside, find `dist/claude/ai-chief-of-staff/`. That folder is the whole system. Copy it, as a folder, to wherever Path A step 2 says it should live. Keep the name exactly `ai-chief-of-staff`. Every behaviour refers to files by name.

**Step 3.** Point Claude at it. Create a project, and in the project instructions paste the contents of `ai-chief-of-staff/CLAUDE.md`. That file is the operating manual, and every behaviour expects it to have been read first.

**Step 4 (optional).** If you want the behaviours available as named skills rather than as files the AI reads, upload the fourteen ZIPs in `dist/claude/skill-uploads/`, one at a time.

First switch on **Code execution and file creation**. That lives in **Settings > Capabilities** on Free, Pro, and Max, and in **Organization settings > Skills** on Team and Enterprise, where an owner also has to switch **Skills** on before anyone can see the section. Then open **Customize > Skills**, click **+**, choose **+ Create skill**, choose **Upload a skill**, and upload one ZIP. Repeat for the rest, and toggle each on. Uploaded skills stay private to that account unless an owner has turned sharing on. Skip all of this if you would rather keep it simple. The behaviours work either way, because they are also sitting in `ai-chief-of-staff/skills/` where the AI can read them.

**Step 5.** Go to **Run onboarding**, below.

---

## Run onboarding

This is the actual setup. Ten minutes, most of it the leader reading a list and saying "that one's wrong."

Start a session and say:

> **Run onboarding.**

Point it at the folder if it asks. It will:

1. **Create any missing files.** You never have to make one by hand.
2. **Check what it can reach** and write that down.
3. **Draft the leader's profile** from the calendar, sent mail, and documents. Everything it guessed is labelled `(inferred)`.
4. **Show you what it worked out** in one scannable block and ask what to fix.
5. **Ask six questions**, and only six. They are the things no tool can ever reveal.
6. **Save**, once you approve.

**The corrections are the product.** Every "no, it's actually X" turns a guess into a fact. Do not rush this to get to the brief.

### Then spend twenty more minutes on four answers

Anything still in `[BRACKETS]` after onboarding is a decision nobody has made yet. That is allowed. Four of them do more work than everything else combined: `about-me.md` section 6 (who the leader can never miss), `about-me.md` section 8 (hard stops), `my-work.md` section 1 (what this quarter is actually for), and `my-work.md` section 5 (what they are not doing).

Spend longest on the last one. A system that knows what the leader is avoiding is more useful than one that only knows what they want. `DEPLOY-FOR-A-CLIENT.md` section 4 has the wording that gets a real answer rather than a polite one.

---

## Run the first brief

> **Run the morning brief.**

What good looks like: under 400 words. Starts with the work, not a greeting. Two to four priorities with a reason each. Only the meetings that need something. Every claim traceable to a file or a source, and anything uncertain labelled. `example/briefs/` holds one that hits the mark, if you want something to hold it against. In ChatGPT that folder is not in the project. It is at `dist/chatgpt/example/briefs/` in the unzipped folder on disk, so open it there.

**There should be nothing about connections on day one.** That is correct. The system just set its own timers, so it has nothing to say yet. An empty capability section on the first brief means it is working.

---

## Schedule it

Add **the morning brief only**. Nothing else this week.

`SCHEDULES.md` carries the exact prompt text for every recurring job, on both platforms, plus the week-by-week order to add them in and a worked clock. Copy from there rather than writing your own. Nine of the fourteen behaviours can run on a schedule, across ten tasks, because inbox triage runs twice a day.

**In Claude Cowork.** Type `/schedule` in any task, or open **Scheduled** in the left sidebar and choose **New task**. Set the cadence, the approval mode, and the folder Claude should work in. Cowork scheduled tasks run in the cloud, so they run whether or not the leader's computer is awake.

**In Claude Code.** Use the **Routines** page in the desktop app for a local scheduled task, or `/schedule` for a cloud job. A local task only runs when the machine is on.

Two things catch people out:

- **Most scheduled runs start fresh.** They remember nothing from your conversations, so the prompt has to name the folder every time. ChatGPT monitoring tasks are the exception. They remember earlier runs so they can report only what changed.
- **A scheduled run in the cloud reaches connected sources.** Your hard drive is out of reach. See Path A step 2 on where the folder has to live.

**Do not add the whole ramp on day one.** Nine outputs nobody opens is worse than one that gets read. The transcript sweep exits silently every day until a transcription tool is connected, which is designed rather than broken.

---

## Run it for a week before changing anything

The first week's corrections are the real setup. When it gets a name wrong, mishears a priority, or drafts in the wrong tone, fix the source file rather than the output. That is what makes week two better.

---

## What is in the folder

```
ai-chief-of-staff/
├── CLAUDE.md          The operating manual. Read first on every run.
├── QUICK-START.md     The page you hand the leader. Nothing reads it.
├── connections.md     What the system can reach. It maintains this itself.
├── about-me.md        Who the leader is, how they work, their voice.
├── my-work.md         What is active right now, and what is not.
├── tomorrow.md        The leader's intent for the next working day.
├── commitments.md     Open promises, both directions.
├── decisions.md       Calls the leader closed, and what would reopen each one.
├── skills/            The fourteen behaviours.
├── example/           A filled-in workspace for a leader who does not exist.
├── briefs/            Output. Briefs, closes, reviews, drafts.
├── meetings/          Output. One folder per meeting.
├── people/            Output. One file per person who matters.
└── archive/           Output. Closed commitments, resolved loops.
```

Five files the leader owns. One file the system owns. Thirteen behaviours. One worked example. Four folders that fill themselves.

That tree is the Path B folder, and Path B is the only path where all of it sits in one place. Three lines to save a consultant a debugging session at minute 58:

- **Path A has no `skills/` folder.** The behaviours are installed in the plugin, not copied into the workspace. Nothing is missing.
- **Path A has no `example/` folder either.** The worked example stays in the downloaded repository. The folder starts empty and `onboarding` writes the seven workspace files and the four output folders into it, which is what its step 0 is for.
- **Path A has no `QUICK-START.md` either.** The plugin ships behaviours, and `onboarding` writes the workspace files. Neither of them writes the handover page. It is at the top of the downloaded repository, and it is also inside `dist/claude/ai-chief-of-staff/` if you took Path B. Hand the leader whichever copy you have.

### Three things worth understanding

**`connections.md` is not yours to fill.** Every other file is written by the leader and read by the system. This one is the reverse. It exists so the system can tell the difference between "no meetings had transcripts yesterday" and "there is no transcription tool connected." Those look identical in the output and they are completely different problems. It tracks capabilities rather than vendors. "Transcripts" is a row, and Otter, Fathom, Fireflies, Granola, and Grain are things that can fill it. Swap the tool, change one cell, and nothing else needs editing.

**`decisions.md` is a record, not a plan.** The system drafts an entry after the leader closes a call, and it never writes an outcome the leader has not said out loud in that session. Once an entry reads `Made`, the reasoning in it is never edited, including where it turned out to be wrong. The field that earns the file its keep is **Would change my mind**, because the Monday review pass is the only thing in the system that checks whether a July decision still matches September's facts.

**Nudges are rare on purpose.** When a tool is missing, the system can mention it. Three gates have to pass first: enough time since the last mention, the leader has not said stop, and something happened that day where the missing tool would actually have helped. That third gate is the one that matters. Being overdue is not a reason to speak. Most mornings there is nothing, and the section does not appear at all.

The exception is a fault. If a connected tool quietly stops working, that gets flagged immediately, every time. A missing tool is a gap the leader knows about. A broken one is a gap they do not.

---

## Adding a tool later

Connect it. Do nothing else.

The next connection check notices, and the next morning brief says one line:

> You connected Fathom. Want me to start the daily sweep, so tomorrow's meetings come back as action items?

Say yes and the behaviour turns on. Say no and it does not come up again. The system will not switch anything on by itself, because a tool appearing in an account is not the same as the leader asking for a behaviour.

---

## If something goes wrong

**Start by saying "Check the setup."** That runs `health-check`. It reads every file, tests what it can reach, and returns one verdict plus a ranked list: blocking gaps, stale files, contradictions between files, output folders that are not filling. It diagnoses most of the table below on its own, and it edits nothing.

| What you see | What it usually is |
|--------------|-------------------|
| The brief runs long, or opens with "Good morning!" | The operating manual is not being read. Check it is in the project instructions and the session is inside the project. |
| Priorities are generic | `my-work.md` section 2 is still bracketed. Fill it in. |
| It can read files but cannot save them | Write access is not enabled for the storage connector. |
| "(not connected)" about the calendar | The connector dropped or the token expired. Reconnect it. |

| A scheduled task produces nothing useful | The prompt does not name the folder, or the folder sits somewhere a cloud run cannot reach. Path A step 2. |

| A ChatGPT scheduled task stopped arriving | It paused itself, or the chat it belonged to was deleted. Open the **Scheduled** page. |
| It invents a meeting detail | Serious. Note the exact line and open an issue. That is a defect, not a setting. |
| It offers to connect something for you | Same. It is never allowed to authenticate anything. |

---

## Making it yours

You are meant to edit this. See `CREDITS.md` for the terms, which are short and permissive.

If you only change one thing, change `CLAUDE.md` section 6 so the voice rules match the house style of whoever is using it.

If you are going to maintain your own version, edit the files in `src/` and run `python3 build/build.py`. That regenerates the Claude and ChatGPT versions together, so they never drift apart. See `README.md` for how the build works.

---

*Created by The NoW of Work. MIT licensed. Yours to edit, adapt, and rename.*
