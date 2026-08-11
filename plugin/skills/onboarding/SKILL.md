---
name: onboarding
description: "Set up the AI Chief of Staff. Creates any missing workspace files, detects connected tools, drafts about-me.md and my-work.md from real sources, then asks only what no tool can reveal."
---

# onboarding

## Trigger

- Once, at deployment, before any other behaviour runs.
- Again whenever the leader changes role, organization, or tool stack.
- On demand: "run onboarding", "set this up", "set this up again", "my details are out of date".
- Automatically offered when the workspace files are missing, when `connections.md` has every row reading `unknown`, or when `about-me.md` still has `[LEADER NAME]` in it.

## The rule this behaviour exists to enforce

**Infer first, ask last, and only ask what matters.**

A setup wizard that asks thirty questions gets abandoned at question nine. Most of those thirty answers are already sitting in the leader's calendar, mail, and documents. Go and get them. Save the leader's typing for the six things that no connected source will ever tell you: what they always want flagged, what you must never do, what this quarter is actually for, what they are deliberately not doing, what time to defend, and what question to ask when two things want the same hour.

Cap the first run at **six question clusters**. If you are about to ask a seventh, you are asking something you should have inferred.

## Reading order

1. `CLAUDE.md`.
2. `connections.md`, if it exists.
3. Whatever already exists in `about-me.md` and `my-work.md`. Never overwrite a confirmed value with an inferred one.

---

## Step 0: Scaffold the workspace

**Do this before anything else, every run.** Onboarding is responsible for making sure the workspace exists. The leader should never have to create a file by hand.

Check for each of these. Create anything that is missing. Never overwrite anything that is already there.

| Path | If missing |
|------|-----------|
| `CLAUDE.md` | Copy from `templates/CLAUDE.md` in this skill folder |
| `about-me.md` | Copy from `templates/about-me.md` |
| `my-work.md` | Copy from `templates/my-work.md` |
| `tomorrow.md` | Copy from `templates/tomorrow.md` |
| `commitments.md` | Copy from `templates/commitments.md` |
| `decisions.md` | Copy from `templates/decisions.md` |
| `connections.md` | Copy from `templates/connections.md` |
| `briefs/README.md` | Create the folder and the stub |
| `meetings/README.md` | Create the folder and the stub |
| `people/README.md` | Create the folder and the stub |
| `archive/README.md` | Create the folder and the stub |

The blank templates ship alongside this file, in `templates/`. Read them from there rather than writing them from memory, so every deployment starts from the same known-good text.

If a file exists but is empty, treat it as missing and write the template into it.

Report what you created in one line, then move on:

```
Workspace ready. Created: connections.md, tomorrow.md, decisions.md, briefs/, meetings/,
people/, archive/.
Already there: CLAUDE.md, about-me.md, my-work.md, commitments.md.
```

If nothing was missing, say `Workspace already in place.` and move on. Do not make a paragraph of it.

## Step 1: Detect

Work out what this system can actually reach, and write it to `connections.md`.

Probe every capability read-only. One cheap call each. List the calendars, list one page of recent mail, list a few recent documents, list the last few transcripts. You are not reading the content yet. You are answering one question per row: does this respond.

If you are running somewhere that cannot see its own connectors, ask once, in a single message, which of the seven capabilities the leader has. Then confirm each claimed one by trying to read from it. A tool the leader says is connected but that returns nothing is `failing`, not `connected`, and that distinction is worth more than their answer.

For each capability, write `connected`, `missing`, or `failing`, plus the provider name and today's date in Last verified.

Report the result as a short list before moving on. The leader should see the shape of what you found:

```
Connected: Calendar, Email, Documents
Missing:   Transcripts, Chat, Tasks, CRM
```

Do not nudge about the missing ones now. Onboarding is not the moment. `connection-check` owns that, and it will not raise anything for at least one cadence.

## Step 2: Auto-fill

From the connected sources only, draft `about-me.md` and `my-work.md`. Label every inferred field `(inferred)`.

| What to fill | Where it comes from | How |
|-------------|---------------------|-----|
| Name, email, title, organization | Calendar or mail account identity, mail signature | Read it. Do not guess a title from a job posting. |
| Time zone | Calendar settings | Read it. |
| Working rhythm: deep-work blocks, meeting-friendly hours, hard stop | Last 4 weeks of calendar | Find the recurring empty windows and the hour after which nothing is ever booked. |
| Days or windows the leader avoids meetings | Last 4 weeks of calendar | Look for consistently blank slots that are blank on purpose. |
| Default meeting length | Calendar | The modal duration. |
| Key relationships | Recurring meeting attendees, ranked by frequency and recency | Top 6 to 8 external and internal names. Relationship type is a guess. Say so. |
| Voice traits | The leader's own sent mail, 15 to 20 messages, external recipients | Sentence length, greeting and sign-off habits, formality, words they actually use. Quote two real sentences back as evidence. |
| Words and tics they avoid | Same sample | If they never write "reach out" or "circle back", that is worth recording. |
| Tone by recipient | Same sample, grouped by recipient domain | Client, internal, board, cold. |
| The business, who it serves, how it makes money | Email domain, website, documents, recurring deck or proposal titles | One sentence each. |
| Current scale | Documents, only if stated plainly | If you cannot find a number, leave it blank. Never estimate. |
| Active priorities | Document titles and edit recency, recurring project meetings, subject lines over the last 6 weeks | Propose up to five. These are the leader's to correct. |
| Names, terms, spelling | Documents and sent mail | Note which spelling convention they actually write in. |

Rules for this step:

- **Never infer** the always-flag list, the hard stops, the current strategic priority, or the not-doing list. Those four are decisions, not facts. They get asked in step 4.
- **Never infer** a number. Revenue, headcount, pricing, follower count. If it is not written down in plain text, leave it blank.
- **Never infer** anything personal or sensitive about a third party. Names and roles only.
- If a capability is `missing`, leave everything sourced from it blank and note which section is thin because of it. Do not backfill from imagination.

If nothing at all is connected, skip to step 4 and say so plainly: "I cannot read anything yet, so I am going to ask instead of guess. Six questions."

## Step 3: Confirm

Show the leader one scannable block of everything you worked out. This is the only long output onboarding produces, and it is a list, not prose.

Group by file. One line per field. Mark each line so the leader can act on it in one word:

```
ABOUT-ME

  Name          Dana Okonkwo                                    [ok / fix]
  Title         VP Operations                       (inferred)  [ok / fix]
  Time zone     America/Vancouver                               [ok / fix]
  Deep work     08:00-10:00, Tue Wed Thu            (inferred)  [ok / fix]
  Hard stop     Nothing booked after 16:30          (inferred)  [ok / fix]
  Voice         Short sentences. No greeting on internal mail.
                Signs off "Thanks, D."              (inferred)  [ok / fix]

MY-WORK

  Business      Regional logistics, 3PL for grocery (inferred)  [ok / fix]
  Priority 1    Warehouse automation pilot          (inferred)  [ok / fix / cut]
  ...

KEY RELATIONSHIPS                                               [ok / fix / cut]

  Marcus Reyes      weekly 1:1        (inferred: direct report)
  Priya Anand       biweekly          (inferred: client)
```

Then ask one question: **"Anything to fix or cut?"**

Take the corrections. A corrected field loses its `(inferred)` label and becomes confirmed. A field the leader says nothing about keeps its label, because silence is not confirmation.

Do not argue with a correction. Do not ask why. Write it down.

## Step 4: Ask the gaps

Only now, and only these. Six clusters, hard cap. Ask them in one message so the leader can answer in one pass.

1. **Always flag.** "What should I surface every single time, even when the day is busy? People, topics, deadline windows."
2. **Hard stops.** "What must I never do? Send without approval, draft in someone else's voice, store certain kinds of detail."
3. **This quarter.** "What is the one thing the business is trying to do right now?"
4. **Not doing.** "What keeps pulling your attention that should not? I will flag it as drift when it shows up."
5. **Protect.** "What time do I defend when someone asks for it?"
6. **Decision filter.** "When two things compete for the same hour, what is the first question I should ask?"

If the leader answers three of six and stops, take the three. A partly filled workspace that gets used beats a complete one that never got finished. Note the gaps and offer to pick them up in the first weekly review.

## Step 5: Save

Write the confirmed and inferred values into `about-me.md`, `my-work.md`, and `connections.md`. Keep the `(inferred)` labels in the files. They are how the system knows what it is still standing on a guess about.

Write today's date into `Last nudged` for every capability recorded as `missing`. This starts each nudge clock at setup, so the first possible mention of a gap is one full cadence away. Without this the gate reads an empty `Last nudged` as "never nudged, go ahead" and the leader gets a nudge the morning after setup, which is the exact behaviour this system is built to avoid.

Every write is approval-gated. Show what you are about to save, get a yes, then save.

Then hand off to `health-check` and run it, on this run and on every re-run. It reads the workspace as a whole and reports what setup left behind, including any of the four fields still bracketed. This behaviour does not audit its own output, and the leader is in the room now, which is the only time a bracketed field can be filled.

Finish with two lines:

```
Setup saved. Anything still marked (inferred) will get corrected as we go.
Want me to run tomorrow's morning brief so you can see what this produces?
```

---

## What this behaviour must never do

- Connect, authenticate, or install anything. It reports what it found. The leader wires tools up outside this workspace.
- Nudge about a missing capability. Not once, not gently. That is `connection-check`'s job and its clock has not started.
- Overwrite a value the leader confirmed on a previous run with a fresh inference.
- Overwrite a workspace file that already has content in it.
- Ask more than six question clusters on the first run.
- Write a personal or sensitive detail about anyone into `people/`.

## Re-running

On a re-run, skip what is already confirmed. Re-probe every capability, because that is the part that goes stale fastest. Show a diff, not the whole block:

```
Since last setup:
  Transcripts   missing -> connected (Fathom)
  Priority 3    "Hiring plan" looks finished. Cut it?
```

Two lines of change beat a full re-confirmation the leader will skim.
