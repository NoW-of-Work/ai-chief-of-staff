> **Example file, read-only.** Invented leader, invented company. The leader's own files live in the workspace root, not in this folder.

# decisions.md — Decision Log

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

---

## Live decisions

### [2026-03-13] Whether the net revenue retention line in the data room carries a stated Fairloch assumption

- **Status:** Open
- **Forced by:** Hannah Sorbara locks the deck on Mar 18. The data room opens Mar 20, four days before the Fairloch renewal decision exists.
- **Would change my mind:** Denise Okafor puts her board's requirements in writing before Mar 18, which turns the assumption into a fact. / Gord Aylward moves the data room date, which he would say by Mar 18.
- **Review on:** 2026-03-18
- **Source:** email thread, "NRR line, need your call"

### [2026-03-12] Whether the Fairloch renewal is 12 months with a service credit or a 6-month extension

- **Status:** Open
- **Forced by:** Denise Okafor reports to her board on Mar 31 and the contract expires Apr 30.
- **Would change my mind:** Engineering commits to a Depot Sync ship date inside April, confirmed by Devin Osei on Mar 19. / Denise says in writing that her board will not accept an extension, expected by Mar 16.
- **Review on:** 2026-03-24
- **Source:** meetings/2026-03-12-fairloch-options/notes.md

### [2026-03-09] Whether a service credit for the December outage was offered to Fairloch

- **Status:** To verify
- **Forced by:** The Mar 9 escalation call. Fathom returned no transcript, the wording in the notes reads both ways, and Denise may be holding us to it.
- **Review on:** 2026-03-17
- **Source:** meetings/2026-03-09-fairloch-escalation/notes.md

The matching `[To verify]` line sits in `commitments.md` for the same date. One is the decision, one is the promise, and neither is confirmed. This entry carries no conditions under **Would change my mind**. There is nothing confirmed to set them against, and only the leader can clear it.

### [2026-03-06] Whether the Depot Sync multi-depot report jumps the engineering queue

- **Status:** Made
- **Forced by:** Renée Lachapelle needed a queue answer before the Mar 9 escalation call, where Fairloch would ask for a ship date.
- **Chose:** Depot Sync goes ahead of the Braemar and Cordell go-lives.
- **Because:** "The report is contract language. The two go-lives are a promise about a date, and I can move a date."
- **Passed on:** Holding the queue, which keeps two go-lives inside the 45-day contract promise and leaves the renewal with nothing to point at.
- **Would change my mind:** Braemar escalates the slip above Alan Whitcombe, watched to Mar 31. / Fairloch signs before the report ships, known by Apr 30.
- **Review on:** 2026-03-31
- **Source:** meetings/2026-03-06-fairloch-plan/notes.md

### [2026-03-05] Whether to offer the Director of Implementation Delivery role to Yusuf Adeyemi

- **Status:** Open
- **Forced by:** Yusuf asked for an answer by Mar 17 and has a second offer in hand.
- **Would change my mind:** The second finalist accepts the same band, which the recruiter would know by Mar 17. / Devin Osei says he can hand route template configuration to two people this quarter, testable at the Mar 17 weekly.
- **Review on:** 2026-03-17
- **Source:** meetings/2026-03-05-hiring-panel/notes.md

### [2026-03-02] Whether to rebuild the support ticket taxonomy this quarter

- **Status:** Made
- **Forced by:** Renée Lachapelle put it in the Q2 plan and needed a yes or a no before staffing it.
- **Chose:** Parked to July 1. Nothing starts before then.
- **Because:** "It is real work and it does not move retention before the data room opens. I would rather say July than say yes and mean never."
- **Passed on:** Starting now, which takes two of Renée's people off Fairloch for three weeks. Cancelling it outright, which costs the goodwill of the person who has carried the escalation alone since February.
- **Would change my mind:** Tickets per customer rise above the January baseline, checked May 1. / A renewal is lost with the taxonomy named as a reason, known any time.
- **Review on:** 2026-07-01
- **Source:** meetings/2026-03-02-cs-weekly/notes.md

### [2026-02-26] Whether implementation becomes its own function reporting to the COO

- **Status:** Open
- **Forced by:** Renée Lachapelle raised it on Feb 26. It blocks the reporting line in the Director of Implementation Delivery offer.
- **Would change my mind:** The go-live average drops below 60 days with no structure change, measured Apr 30. / The new director starts and the 11-account backlog clears under the current structure, reviewed Jun 1.
- **Review on:** 2026-04-01
- **Source:** meetings/2026-02-26-cs-monthly/notes.md

### [2026-02-13] Whether customers under 60 trucks stay in the pipeline

- **Status:** Made
- **Supersedes:** [2026-01-19] Whether to stop selling to customers under 60 trucks
- **Forced by:** The exec offsite on Feb 13, with two under-60 deals held since January.
- **Chose:** They stay, with implementation capped at one per month.
- **Because:** "The cost was never the segment. It was the capacity. Cap the intake and the problem goes away without cutting a third of the customer base."
- **Passed on:** Cutting the segment, which removes 31% of customers and 9% of revenue and changes every cohort chart in the deck. Leaving intake uncapped, which holds the go-live average above 74 days.
- **Would change my mind:** The monthly cap is breached twice in one quarter, checked Jun 30. / Under-60 customers churn above the book average, measured at the Jun 30 renewals.
- **Review on:** 2026-06-30
- **Source:** meetings/2026-02-13-exec-offsite/notes.md

### [2026-01-27] Whether to connect every available source at onboarding or start with three

- **Status:** Made
- **Forced by:** Onboarding ran Jan 27 and every capability had to be probed or left at `missing` in the same session.
- **Chose:** Start with calendar, mail, and documents. Add one source at a time, each with a reason.
- **Because:** "Three sources that already work beat seven that half work. I will add the others when something breaks for want of them."
- **Passed on:** Connecting everything at once, which would have put four unverified sources under the morning brief with nothing to show which one was lying. Fathom proved the point on Mar 16.
- **Would change my mind:** Two capabilities read `failing` at the same time, which would mean the count is the problem rather than the tool, watched continuously. / A brief labels something `(not connected)` twice in one week for a priority named in `my-work.md`, checked at the weekly review.
- **Review on:** 2026-04-27
- **Source:** meetings/2026-01-27-onboarding/notes.md

### [2026-01-22] Whether to change the pricing model before the raise

- **Status:** Stood
- **Forced by:** Gord Aylward wanted per-seat pricing in the deck and the data room date was already set.
- **Chose:** Pricing stays per depot plus per vehicle through the raise.
- **Because:** "Changing the model mid-raise invalidates the cohort charts. We can price differently in a company that has already closed."
- **Passed on:** Per-seat pricing, which reads better to a software investor and costs the comparability of every chart back to 2024.
- **Would change my mind:** Two or more deals are lost on pricing structure rather than price, checked Mar 1. / The raise closes, which removes the reason to wait.
- **Review on:** 2026-06-01
- **Source:** meetings/2026-01-22-pricing-review/notes.md

### [2026-01-19] Whether to stop selling to customers under 60 trucks

- **Status:** Superseded
- **Forced by:** The January board pack asked why implementation cost per customer was flat across segment sizes.
- **Chose:** Stop selling under 60 trucks from Feb 1.
- **Because:** "They cost what a large customer costs and pay a ninth of it. I could not defend the segment in the room."
- **Passed on:** Capping intake, which nobody had costed at the time. Doing nothing, which leaves the implementation queue where it is.
- **Would change my mind:** Someone shows a way to hold implementation cost flat without cutting the segment, by Feb 13. / Under-60 customers turn out to renew above the book average, checked at Feb 13.
- **Review on:** 2026-02-13
- **Source:** meetings/2026-01-19-board-prep/notes.md

> Reopened 2026-02-13: the first condition fired. Devin Osei costed a one-per-month intake cap at the exec offsite and it held implementation cost flat without cutting the segment.
> Superseded 2026-02-13 by [2026-02-13] Whether customers under 60 trucks stay in the pipeline.

---

## Reopening a decision

The point of this file is the second reading. A decision made in January was made against January's facts. When those facts move, the decision should get another look on purpose rather than by accident.

Reopen when either of these happens:

1. A condition under **Would change my mind** comes true.
2. The **Review on** date arrives and the assumptions no longer hold.

Then, in order:

1. Change the original entry's status to `Reopened`. Leave every other field exactly as written.
2. Append one line to the original entry, below the fields: `> Reopened YYYY-MM-DD: [which condition fired, and the evidence].`
3. Write the new decision as a new entry, carrying `**Supersedes:** [YYYY-MM-DD] [original title]`.
4. Change the original entry's status to `Superseded` once the new one is `Made`.

If the review date arrives and nothing has moved, mark the entry `Stood`, set a new **Review on** date, and say nothing about it in the brief. A decision that is still correct is not news. The pricing entry was reviewed on Mar 2, held, and went to Jun 1 without appearing in a single brief.

---

## Superseded and archived

Superseded entries stay in this file for 180 days so the trail is readable in one place. After that, move them to `archive/decisions-[YYYY]-Q[N].md`, keeping every field and the reopening line intact.

Never delete an entry. The reasoning is the asset, including the reasoning that turned out to be wrong. The Jan 19 entry above is the clearest thing in this file, and it is the one that was wrong.

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

## The Monday pass

`decision-brief` reads this file on its Monday run, before the morning brief, and surfaces:

- Any entry whose **Review on** date has passed.
- Any entry where a condition under **Would change my mind** has come true, with the evidence.
- Any `Open` entry whose **Forced by** date lands in the next 14 days.
- Any `To verify` entry still waiting on the leader.

Nothing else from this file appears in a brief. A decision that is holding needs no airtime.

As of 2026-03-17 that scan returns four `Open` entries, three of them with a **Forced by** date inside 14 days, and one `To verify` entry open for eight days. No condition under **Would change my mind** fired this week. The Fairloch entry's second condition is overdue rather than fired: the writing expected from Denise Okafor on Mar 16 has not arrived, and that absence is itself the thing to raise.
