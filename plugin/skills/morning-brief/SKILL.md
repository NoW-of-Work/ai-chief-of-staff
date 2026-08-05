---
name: morning-brief
description: "Start-of-day brief: today's priorities, meetings needing something, open loops, drafts awaiting a yes, and one capability line if there is one. 400 words. Use when asked what today looks like."
---

# morning-brief

## Trigger

- Start of the working day, on a schedule.
- On demand: "what does today look like", "brief me", "morning brief".

## The rule

**400 words, hard cap.** A 250-word brief that gets read every morning beats a 1,000-word brief that gets skipped three days a week. When you run over, cut in this order:

1. The capability nudge or offer line goes first. A fault line is never dropped.
2. Then background context on meetings.
3. Then open loops that are not due this week.
4. **Never the priorities.** They are the reason the brief exists.

## Reading order

1. `CLAUDE.md`.
2. `connections.md`. Two things: which sources exist today, and whether there is a queued nudge or activation offer to render.
3. `tomorrow.md`. This is the leader's own statement of intent and it outranks everything else you are about to read.
4. `about-me.md`, sections 6 and 7 especially (always flag, always protect).
5. `my-work.md`, sections 2 and 5 (active priorities, and what they are not doing).
6. `commitments.md`.
7. Today's calendar. Yesterday's mail since the last brief.

If `tomorrow.md` is written for a date that is not today, say so in one clause and use it anyway if it is recent. Do not silently ignore it.

---

## Structure

Render slots in this order. **A slot with nothing in it does not render at all.** No headings with "nothing today" underneath. Empty sections train the leader to skim.

### 1. Today, in one line

What the day is actually for. Pulled from `tomorrow.md` "Must respect" if it exists, otherwise from the top of `my-work.md` priorities.

### 2. Priorities (2 to 4)

What earns the leader's attention today, in order. Each one is a line: the thing, and why it is today's problem rather than tomorrow's. Name the tradeoff when two compete.

Use the decision filters in `about-me.md` section 4 and the tradeoff defaults in `my-work.md` section 7. If `tomorrow.md` disagrees with both, `tomorrow.md` wins.

### 3. Calendar

Only what needs something from the leader. A meeting they attend and do not prepare for does not need a line.

For each: time, who, and the one thing that would make it go better. Flag anything in the always-flag list from `about-me.md`. Flag anything intruding on a protected block, with an alternative to propose.

If a high-stakes meeting has no prep, say so and offer to run `meeting-prep`.

### 4. Open loops

From `commitments.md`. Only what is due in the next 48 hours, stale past the thresholds, or attached to someone in the always-flag list. Not the whole ledger. The leader reads the whole ledger in the weekly review.

### 5. Drafts waiting

Anything you drafted that needs a yes or a no. One line each. Link or filename.

### 6. Capability check

**At most one nudge or one offer, never both, never two of either.** A fault line is separate and always renders alongside. Read from the queue that `connection-check` wrote. Three things can appear here:

**An activation offer**, when the leader connected something:

> You connected Fathom. Want me to start the daily sweep, so tomorrow's meetings come back as action items?

**A fault**, when something connected has silently stopped working. This is the one that does not count against the cap and always renders:

> Otter has not returned a transcript since July 3. Three weeks of meetings did not get swept.

**A nudge**, when a missing tool cost the leader something specific yesterday:

> You had four meetings yesterday with nothing capturing them. A transcription tool that records where you meet (Grain, Otter, Fathom) would let me pull the action items automatically. I will not raise this again for two weeks.

If both a nudge and an offer are queued, the **offer wins**. It is news, and it is the one the leader can act on today. The nudge waits for its next cadence window.

If the queue is empty, **this slot does not render.** No "everything is connected." No green checkmarks. Most mornings there is nothing here and that is the system working.

After rendering a nudge, write today's date into `Last nudged` for that capability in `connections.md`. After rendering an offer, leave it pending until the leader answers, then mark it accepted or declined.

### 7. What I could not see

One line, only when it matters. Distinguish the two cases using the labels from `CLAUDE.md` section 7:

- `(no source)` means the leader has a gap in their notes.
- `(not connected)` means the system has a gap in its wiring. Do not turn this into a second nudge. The capability slot already had its one shot.

---

## Voice

Follow `about-me.md`. Defaults: short sentences, active voice, no hype words, no em dashes, no "not X but Y" contrasts.

Write like a person who read everything and is telling the leader the part that matters. Not like a report.

Do not open with a greeting or the date. The leader knows what day it is. Start with the work.

## Approval rules

- May save the brief to `briefs/YYYY-MM-DD.md`.
- May update nudge dates and offer statuses in `connections.md`.
- May not send anything, book anything, or reply to anything.
- May not act on an activation offer. Rendering the offer and recording the answer is the whole job. Turning the behaviour on happens in a session where the leader is present, per `CLAUDE.md` gate 9.
- May not render a **nudge** for a capability the registry marks `Dismissed`. An activation offer for a dismissed capability that has since been connected still renders, because that is news rather than nagging.

## Worked example

```
Today is about getting the Ridley proposal out before the 15:00 call.

PRIORITIES
1. Ridley proposal, final pass. Due today. Nothing else on the list has a date.
2. Marcus 1:1 prep. He flagged the hiring plan twice last week and you have not
   answered. (source: commitments.md, awaiting since Jul 14)
3. Quarterly planning doc can wait. It has no external dependency this week.

CALENDAR
  09:00  Deep work block. Someone has requested this slot. Propose 16:00 instead?
  11:00  Priya Anand (Ridley). No prep on file. Want me to pull it together?
  15:00  Ridley call. This is the one the proposal is for.

OPEN LOOPS
  Marcus, hiring plan answer, awaiting 9 days.
  Sven, contract redline, due tomorrow.

DRAFTS WAITING
  Reply to Priya re: timeline. briefs/2026-07-23-draft-priya-timeline.md

CAPABILITY
  You had four meetings yesterday with nothing capturing them. A transcription
  tool that records where you meet (Grain, Otter, Fathom) would let me pull the
  action items automatically. I will not raise this again for two weeks.
```

Under 400 words. Every claim has a source or a label. The capability line names yesterday's actual cost and promises to go quiet.
