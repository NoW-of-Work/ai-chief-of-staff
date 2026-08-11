# decisions.md — Decision Log

> **Template note.** This file records decisions the leader actually made, and the reasoning underneath them. It is not a task list and not a project tracker. An entry exists here because a real choice was closed, and because the reasoning behind it will be worth reading again when circumstances move.
>
> The `decision-brief` behaviour drafts entries after the leader decides, and it is the only behaviour that writes here. It never writes an outcome the leader has not stated. It may open an entry before the decision is made, so the question is on the record with a date attached. The `recall` behaviour reads this file before it reads `meetings/`, and a `Made` entry here outranks the meeting file the decision came from.
>
> The field that makes this file worth keeping is **Would change my mind**. A decision logged without one cannot be revisited. It can only be regretted. Every entry carries two conditions, each with a date or a signal that someone else could check.

---

## Status taxonomy

- **Open** — the question is named and dated, and nothing has been decided yet.
- **Made** — decided, with the option chosen and the reasoning recorded.
- **Reopened** — a condition under **Would change my mind** came true, or the review date arrived and the assumptions had moved.
- **Superseded** — a later decision replaced this one. Points forward to the entry that replaced it.
- **Stood** — reviewed on its review date, assumptions held, no change made.
- **To verify** — the AI Chief of Staff believes a decision was made and cannot confirm it. Needs leader review.

---

## Format

One block per decision. Fields in this order, every time, so the file can be scanned by field rather than read end to end.

```
### [YYYY-MM-DD] [The decision, as a choice, in one sentence]

- **Status:** [Open / Made / Reopened / Superseded / Stood / To verify]
- **Forced by:** [What put a date on it. Meeting, offer expiry, deadline, budget cycle.]
- **Chose:** [The option taken, in one line. Deciding nothing yet is a valid answer.]
- **Because:** [The leader's reasoning, in the leader's own words where they exist.]
- **Passed on:** [The options not taken. One line each, with the cost of each.]
- **Would change my mind:** [Condition 1, with a date or a signal.] / [Condition 2, same.]
- **Review on:** [YYYY-MM-DD]
- **Source:** [briefs/YYYY-MM-DD-decision-[slug].md, or "leader, in session, YYYY-MM-DD"]
```

An `Open` entry carries **Forced by**, **Would change my mind** if the conditions are already known, and **Review on**. The rest stay blank until the leader decides.

A filled entry looks like this:

```
### [2026-07-24] Whether to take the Halvorsen retainer at 40 hours a month

- **Status:** Made
- **Forced by:** Halvorsen asked for an answer by Jul 31, with two other firms bidding.
- **Chose:** Countered at 20 hours a month over nine months.
- **Because:** "Teale is the client who pays us today. I am not trading a live
  rollout for a bigger logo."
- **Passed on:** 40 hours as offered, which slips Teale phase two by a quarter.
  Waiting until Aug 8, which risks the offer lapsing.
- **Would change my mind:** Halvorsen refuses any counter, known by Jul 28. /
  Teale phase two is cancelled, which Dana Okonjo confirms by Aug 8.
- **Review on:** 2026-08-11
- **Source:** briefs/2026-07-24-decision-halvorsen-retainer.md
```

---

## Live decisions

Entries land here as the leader decides. Newest first. Empty until the first decision is logged.

---

## Reopening a decision

The point of this file is the second reading. A decision made in July was made against July's facts. When those facts move, the decision should get another look on purpose rather than by accident.

Reopen when either of these happens:

1. A condition under **Would change my mind** comes true.
2. The **Review on** date arrives and the assumptions no longer hold.

Then, in order:

1. Change the original entry's status to `Reopened`. Leave every other field exactly as written.
2. Append one line to the original entry, below the fields: `> Reopened YYYY-MM-DD: [which condition fired, and the evidence].`
3. Write the new decision as a new entry, carrying `**Supersedes:** [YYYY-MM-DD] [original title]`.
4. Change the original entry's status to `Superseded` once the new one is `Made`.

If the review date arrives and nothing has moved, mark the entry `Stood`, set a new **Review on** date, and say nothing about it in the brief. A decision that is still correct is not news.

---

## Superseded and archived

Superseded entries stay in this file for 180 days so the trail is readable in one place. After that, move them to `archive/decisions-[YYYY]-Q[N].md`, keeping every field and the reopening line intact.

Never delete an entry. The reasoning is the asset, including the reasoning that turned out to be wrong.

---

## Rules the AI Chief of Staff must follow

1. **No outcome without the leader saying it.** If the leader has not decided, write `Open`. If you believe they decided and cannot find them saying so, write `To verify` and quote what made you think it. Leaning towards an option is neither.
2. **No entry without two conditions in Would change my mind.** Each one needs a date or a checkable signal. "If things change" is not a condition and does not count as one.
3. **Record the leader's reasoning, not the recommendation.** If the leader decided against the brief, the brief is already filed and says why. This field holds their words. If they gave none, write `(no source)`.
4. **Never edit the fields of a `Made` entry.** Two things may change on it and nothing else: the **Status** line, and one appended reopening line below the fields. **Chose**, **Because**, and **Passed on** stay exactly as written, including where they turned out to be wrong.
5. **Name the cost of every option passed on.** An entry that lists the roads not taken without their prices is unusable at review time.
6. **Never delete an entry.** Statuses move. Rows stay.
7. **A decision reached in a room is not a decision until it is confirmed here.** A meeting file may record an outcome on a question this file carries as `Open`. Draft the entry, show it, ask. Do not promote it yourself.

---

## Weekly review

Every Monday the AI Chief of Staff scans this file and surfaces:

- Any entry whose **Review on** date has passed.
- Any entry where a condition under **Would change my mind** has come true, with the evidence.
- Any `Open` entry whose **Forced by** date lands in the next 14 days.
- Any `To verify` entry still waiting on the leader.

Nothing else from this file appears in a brief. A decision that is holding needs no airtime.
