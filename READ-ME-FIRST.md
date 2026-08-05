# READ ME FIRST

**AI Chief of Staff, v1.0.0. Created by The NoW of Work.**

This is the whole setup guide. If you read one file, read this one.

---

## What you are installing

An AI chief of staff for one leader. It reads the leader's calendar, mail, documents, and meeting notes, and it produces a short morning brief, prep before meetings that matter, action items out of recorded calls, a ledger of open promises, and a Monday review.

It works from six plain text files that the leader owns and can edit. There is no database, no account to create, and nothing that runs outside the AI tool you already pay for.

**It drafts. It does not send.** No email, no calendar changes, no replies. Everything that touches another person goes through the leader first.

---

## Before you start

Three things, and only the first one is required.

| | What | Why |
|---|------|-----|
| 1 | A paid Claude account, or a ChatGPT account | The system runs inside one of them |
| 2 | A calendar connected to it | Almost everything is built on the calendar |
| 3 | Email connected to it | Open loops, follow-ups, and voice all come from mail |

Anything else (documents, transcripts, chat, tasks, CRM) is optional. The system notices what is missing, works around it, and offers to use new tools when they appear. You do not have to connect everything on day one, and you probably should not.

**One thing worth saying out loud before you start.** Setup reads about twenty of the leader's own sent emails to learn how they write, and four weeks of their calendar to learn their working rhythm. That is somebody's real mailbox. Tell them what it reads before it reads it. If they would rather it did not, setup still works, and they write three bullets about their own voice instead.

---

## Install: pick one path

Three paths. Pick the first one that describes you.

- **Path A — Claude, one command.** Fastest. Use this if you can see a `/plugin` command in Claude Code or Claude Cowork.
- **Path B — Claude, one unzip.** Use this if you would rather not use plugins, or `/plugin` is not available on your account.
- **Path C — ChatGPT.** Use this if the leader lives in ChatGPT.

You only need one. All three end up in the same place.

---

## Path A: Claude, one command

**Step 1.** Open Claude Code or Claude Cowork and run these two lines:

```
/plugin marketplace add nowofwork/ai-chief-of-staff
/plugin install ai-chief-of-staff@now-of-work
```

That installs all eight behaviours at once. If the install summary tells you to run `/reload-plugins`, run it.

They arrive as skills, named after the plugin: `/ai-chief-of-staff:onboarding`, `/ai-chief-of-staff:morning-brief`, and so on. You can also just ask for them in plain language, which is what most people do.

> Replace `nowofwork` with whatever GitHub account or organization this repo actually lives under.

**Step 2.** Make a folder for the workspace, somewhere the AI can read and write it. A folder in the leader's cloud drive is the usual answer, because scheduled tasks can reach cloud storage and cannot reach a folder that only exists on a laptop.

Call it `ai-chief-of-staff`. It can be empty. The next step fills it.

**Step 3.** Go to **Run onboarding**, below.

---

## Path B: Claude, one unzip

**Step 1.** Download this repository as a ZIP (the green **Code** button at the top of the GitHub page, then **Download ZIP**) and unzip it once.

**Step 2.** Inside, find `dist/claude/ai-chief-of-staff/`. That folder is the whole system. Copy it, as a folder, into the leader's cloud drive at the top level.

Keep the name exactly `ai-chief-of-staff`. Every behaviour refers to files by name.

**Step 3.** Point Claude at it. Create a project, and in the project instructions paste the contents of `ai-chief-of-staff/CLAUDE.md`. That file is the operating manual, and every behaviour expects it to have been read first.

**Step 4 (optional).** If you want the behaviours available as named skills rather than as files the AI reads, upload the eight ZIPs in `dist/claude/skill-uploads/` one at a time under **Skills**, and switch each on. Skip this if you would rather keep it simple. The behaviours work either way, because they are also sitting in `ai-chief-of-staff/skills/` where the AI can read them.

**Step 5.** Go to **Run onboarding**, below.

---

## Path C: ChatGPT

**Step 1.** Download this repository as a ZIP and unzip it once. Everything you need is in `dist/chatgpt/`.

**Step 2.** Create a new ChatGPT Project called **AI Chief of Staff**.

**Step 3.** Open `dist/chatgpt/PROJECT-INSTRUCTIONS.md`, copy all of it, and paste it into the project's custom instructions.

**Step 4.** Upload these to the project's files:

- everything in `dist/chatgpt/workspace/` (six files)
- everything in `dist/chatgpt/prompts/` (eight files)

**Step 5.** Go to **Run onboarding**, below.

### What is different in ChatGPT

ChatGPT cannot write files into a folder by itself, and it cannot see which connectors it has. So two things change:

- Where the Claude version saves a file, the ChatGPT version prints it in a code block and the leader saves it back into the project. Slightly more clicking, same result.
- Setup asks which tools are connected instead of working it out. Answer honestly and it will verify by trying.

Everything else (the behaviours, the approval gates, the voice rules, the nudge policy) is identical, because both versions are generated from the same source.

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

Anything still in `[BRACKETS]` after onboarding is a decision nobody has made yet. That is allowed. But four of them do more work than everything else combined:

1. `about-me.md` section 6, **always flag**. Who can the leader never miss.
2. `about-me.md` section 8, **hard stops**. What must this never do.
3. `my-work.md` section 1, **current strategic priority**. The one thing this quarter is for.
4. `my-work.md` section 5, **what we are not doing**.

Spend longest on the last one. A system that knows what the leader is avoiding is more useful than one that only knows what they want.

---

## Run the first brief

> **Run the morning brief.**

What good looks like: under 400 words. Starts with the work, not a greeting. Two to four priorities with a reason each. Only the meetings that need something. Every claim traceable to a file or a source, and anything uncertain labelled.

**There should be nothing about connections on day one.** That is correct. The system just set its own timers, so it has nothing to say yet. An empty capability section on the first brief means it is working.

---

## Schedule it

Add **the morning brief only**. Nothing else this week.

Set a daily task that says:

> Read the `ai-chief-of-staff` folder in my drive. Run the morning-brief behaviour. Save the output to `briefs/` with today's date.

Two things that catch people out:

- **Every scheduled run starts fresh.** It remembers nothing from your conversations. So the prompt has to name the folder every time.
- **Scheduled tasks cannot reach a folder that only lives on a laptop.** If the brief has to arrive before the leader opens their computer, the workspace has to be in cloud storage.

Once the brief has been read five days running, add the rest, one at a time:

| Task | When | Say |
|------|------|-----|
| Connection check | Weekly, Monday, an hour before the brief | Run the `connection-check` behaviour. Update `connections.md`. |
| Transcript sweep | Daily, before the brief | Run the `daily-transcript-sweep` behaviour. |
| End-of-day close | Daily, near the leader's hard stop | Run the `end-of-day-close` behaviour. Draft `tomorrow.md` and ask before saving it. |
| Weekly review | Weekly, Monday morning | Run the `weekly-review` behaviour. |

The transcript sweep exits silently every day until a transcription tool is connected. That is designed, not broken.

**Do not add all five on day one.** Five outputs nobody opens is worse than one that gets read.

---

## Run it for a week before changing anything

The first week's corrections are the real setup. When it gets a name wrong, mishears a priority, or drafts in the wrong tone, fix the source file rather than the output. That is what makes week two better.

---

## What is in the folder

```
ai-chief-of-staff/
├── CLAUDE.md          The operating manual. Read first on every run.
├── connections.md     What the system can reach. It maintains this itself.
├── about-me.md        Who the leader is, how they work, their voice.
├── my-work.md         What is active right now, and what is not.
├── tomorrow.md        The leader's intent for the next working day.
├── commitments.md     Open promises, both directions.
├── skills/            The eight behaviours.
├── briefs/            Output. Briefs, closes, reviews, drafts.
├── meetings/          Output. One folder per meeting.
├── people/            Output. One file per person who matters.
└── archive/           Output. Closed commitments, resolved loops.
```

Four files the leader owns. One file the system owns. Eight behaviours. Four folders that fill themselves.

### Two things worth understanding

**`connections.md` is not yours to fill.** Every other file is written by the leader and read by the system. This one is the reverse. It exists so the system can tell the difference between "no meetings had transcripts yesterday" and "there is no transcription tool connected." Those look identical in the output and they are completely different problems.

It tracks capabilities, not vendors. "Transcripts" is a row. Otter, Fathom, Fireflies, Granola, and Grain are things that can fill it. Swap the tool, change one cell, and nothing else needs editing.

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

| What you see | What it usually is |
|--------------|-------------------|
| The brief runs long, or opens with "Good morning!" | The operating manual is not being read. Check it is in the project instructions and the session is inside the project. |
| Priorities are generic | `my-work.md` section 2 is still bracketed. Fill it in. |
| It can read files but cannot save them | Write access is not enabled for the storage connector. |
| "(not connected)" about the calendar | The connector dropped or the token expired. Reconnect it. |
| A scheduled task produces nothing useful | It is pointed at a folder that only exists on a laptop, or the prompt does not name the folder. |
| It invents a meeting detail | Serious. Note the exact line and open an issue. That is a defect, not a setting. |
| It offers to connect something for you | Same. It is never allowed to authenticate anything. |

---

## Making it yours

You are meant to edit this. See `CREDITS.md` for the terms, which are short and permissive.

If you only change one thing, change `CLAUDE.md` section 6 so the voice rules match the house style of whoever is using it.

If you are going to maintain your own version, edit the files in `src/` and run `python3 build/build.py`. That regenerates the Claude and ChatGPT versions together, so they never drift apart. See `README.md` for how the build works.

---

*Created by The NoW of Work. MIT licensed. Yours to edit, adapt, and rename.*
