---
name: decision-brief
order: 10
description: Structure a live decision: the choice, what is at stake, the options and their costs, the leader's own filters, and a recommendation with two falsifiers. 300 words. Use when a decision is due.
---

# decision-brief

## Trigger

- A decision in `my-work.md` section 4 acquires a date, from a meeting, an offer, or a deadline.
- Monday, ahead of `weekly-review`. Scan `decisions.md` for review dates that have passed and for conditions that have fired.
- When `meeting-prep` names a decision the leader is not ready to make.
- On demand: "help me think this through", "should I do this", "build me a decision brief".

## Why this brief always recommends

A brief that lays out four options and stops has handed the work straight back. The leader already knew there were options. That is why they asked. So this behaviour recommends, every time, and shows the weighing underneath. A recommendation with nothing under it can only be taken or refused.

**300 words, hard cap.** A 300-word brief the leader reads twice on the way into a board call beats a 1,500-word memo they open once and skim. When you run over, cut in this order:

1. Any account of how the decision arrived, wherever it crept in. No slot asks for it and it still shows up. The leader lived through it.
2. Then second-order costs on the options you are not recommending.
3. Then the stakes slot, down to a single line.
4. **Never the recommendation or the reasoning under it.** Without those the brief is a list, and the leader still has all the work.

## Reading order

1. `{{MANUAL}}`.
2. `connections.md`. It settles whether an option with no evidence behind it is one nobody raised, or one sitting in a source you cannot read.
3. `about-me.md`, section 4 (decision filters, in the leader's stated order) and section 1.
4. `my-work.md`, sections 2, 4, 5, and 7.
5. `commitments.md`, filtered to anyone this decision binds either way.
6. `decisions.md`, for any earlier ruling on the same question.
7. `meetings/` and `people/[name].md` for whoever has already argued a side.
8. Live sources last: the calendar entry that forces the date, then mail and transcripts.

If `decisions.md` already holds an entry on this question, this is a reopening. Say so in the first line and read that entry's `Would change my mind` field first.

---

## Structure

300 words. Seven slots. Cut history before you cut options.

### 1. The decision, in one sentence

Phrase it as a choice with a date on it. "Whether to take X, by Y."

If it will not fit in one sentence, the leader is holding two decisions. Cover the earlier one and name the one you set aside.

### 2. What is at stake

Two or three lines. What changes depending on which way this goes. Money, capacity, a relationship, a promise already in `commitments.md`.

Pull from `my-work.md` section 2 and the ledger. If neither says anything, one line labelled `(no source)`. An invented stakes paragraph does not render at all.

### 3. The options

Two to four, numbered. One is always deciding nothing yet, carrying the date on which that stops being available.

If the leader has not stated that date, work it out and label it `(inferred)`.

Do not add an option for balance. Padding makes the recommendation look arbitrary.

If a capability that would surface options is `missing` or `failing` in `connections.md`, write `(not connected)` and name it. A partial list makes the recommendation worth less than it looks.

### 4. What each one costs

One line per option. The cost, not the risk. A risk might happen. A cost happens.

Name the cost that is hardest to reverse. Money comes back. A hire does not un-hire.

If a cost is unknown, write `(needs check)` and name who would know, at the company that holds the answer. An option you cannot cost renders as a question.

### 5. What the leader's own filters say

Run the decision through `about-me.md` section 4 in the stated order, then the tradeoff defaults in `my-work.md` section 7. Quote the filter. Answer it.

This is where the leader's calmer past self gets a vote. It is the slot most likely to point away from your recommendation. Render the one that disagrees first.

### 6. Where this cuts against the no-list

Check every option against `my-work.md` section 5. If one is something the leader wrote down as not this quarter, quote the line and name the option it catches.

The leader wrote section 5 with time to think. They are reading this brief because something is pressing. That gap is the whole reason this slot exists.

If nothing in section 5 touches this decision, **this slot does not render.** A line confirming there is no conflict teaches the leader to skip the slot.

### 7. The recommendation, and what would change it

Two parts. Both are required.

One named option, marked as yours: "My read: option 2." Then two or three lines of reasoning, in the order you weighed it, citing the slots above rather than repeating them.

Then the falsifier. What would have to be true for this to be the wrong call. Exactly two conditions, each with a date or a signal. "If the market shifts" is not one. "If Halvorsen refuses any counter, known by Jul 28" is.

Those two become the `Would change my mind` field in `decisions.md`. Write them so someone outside the room could check them.

---

## Writing to the decision log

`meetings/` holds what was said in the room. `decisions.md` holds what the leader confirmed. `transcript-to-actions` writes the first. This behaviour writes the second, and it is the only one that does.

A room can reach a decision the leader has not confirmed, so a meeting outcome on a question `decisions.md` carries as `Open` is a draft entry and a question, never the answer. That is rule 7 in that file, and `{{MANUAL}}` gate 11 sets the same standard.

When the leader decides, draft the entry in the format the file specifies, carrying the two conditions from slot 7. Show it. Ask. Save on a yes. Its rules 3 and 5 govern the remaining fields.

Once logged, the logged entry wins, which is already how `recall` resolves the two. Two records of one decision are cheap. Two answers to one question are not.

## The weekly decisions pass

The review date is what makes `decisions.md` more than an archive, and nothing checks it unless this behaviour does. On the Monday run, surface the four cases that file lists under its weekly review section.

Each one gets a line and a proposal: reopen it, stand it, or confirm it. Nothing else renders. Most Mondays this pass produces nothing.

Write the pass to `briefs/YYYY-MM-DD-decisions.md` and stop there. `weekly-review` runs after it, reads that file, and renders what it found in its decisions slot. This behaviour decides what is due. The review speaks, the same split `connection-check` and `morning-brief` keep. Nothing here speaks to the leader on a scheduled run.

## Rules

- **Never invent an option.** One no source proposed dilutes the two that are real.
- **Never invent a number.** A cost figure with nothing behind it survives into the log and gets reasoned from later.
- **Never bury the recommendation** inside another slot. One the leader has to hunt for gets skipped.
- Do not soften the contradiction in slot 6. Softening it makes the whole behaviour pointless.
- Do not run this on a decision that belongs to a direct report. Check `about-me.md` section 1. Taking a delegated call back costs the leader the person they delegated it to.

## Approval rules

- May save the brief to `briefs/YYYY-MM-DD-decision-[slug].md`.
- May save the Monday review pass to `briefs/YYYY-MM-DD-decisions.md`. That file is what `weekly-review` reads.
- May append an `Open` entry to `decisions.md` naming the decision and the date that forces it.
- May append sourced entries to `commitments.md` for promises the decision creates, once it is made.
- May change an entry's `Status` to `Reopened`, `Superseded`, or `Stood`, and may append the one reopening line `decisions.md` specifies. No other field on a `Made` entry changes.
- May **not** write an outcome to `decisions.md` without the leader stating what they decided, in the same session. `{{MANUAL}}` gate 11. An inferred decision becomes the record the system reasons from a quarter later.
- May **not** log an outcome from a meeting file alone.
- May not edit `my-work.md` section 5 because a decision contradicts it. `{{MANUAL}}` gate 7. Propose the edit and ask.
- May not send anything, and may not tell anyone the decision was made.

## Worked example

```
DECISION
Whether to take the Halvorsen retainer at 40 hours a month, by Jul 31.

AT STAKE
$18,000 a month for six months, the largest on the books, against
the Teale phase two capacity. (source: my-work.md, section 2)

OPTIONS
1. Take it at 40 hours.
2. Counter at 20 hours over nine months.
3. Decide nothing until Teale confirms, Aug 8.

COSTS
1. Teale phase two slips a quarter. Hardest to reverse.
2. Roughly $9,000 a month less. (needs check: would they accept a counter,
   ask Bev Trang, Halvorsen COO)
3. The offer lapses Jul 31, with two other firms bidding.
   (source: meetings/2026-07-21-halvorsen/notes.md)

YOUR FILTERS
1. "Does this move a priority forward this month?" Points away from my read:
   Halvorsen funds the Q4 hire.
2. "Does this protect a paying client?" Teale pays today. Section 7: revenue
   protection wins unless the new work is dated. It is.

AGAINST THE NO-LIST
my-work.md section 5: "No retainers over 20 hours this quarter."
Option 1 is exactly that.

MY READ
Option 2. Holds the no-list, books revenue.
Wrong if Halvorsen refuses any counter (known Jul 28), or if Teale phase two
is dead (Dana Okonjo confirms, Aug 8).
```

195 words. The first filter argues against the recommendation and the recommendation still stands, which is the only version of that slot worth rendering. A fourth option would have cost the stakes slot its second line. How the offer arrived does not appear anywhere.
