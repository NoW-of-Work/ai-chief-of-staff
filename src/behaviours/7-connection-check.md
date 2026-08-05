---
name: connection-check
order: 7
description: Diff live connectors against connections.md. Update the registry, queue activation offers, flag anything silently broken, and decide (rarely) if a missing tool is worth one line. Weekly.
---

# connection-check

## Trigger

- **Scheduled:** once a week. Monday before the morning brief is a good slot, so anything it finds lands in that day's brief.
- **Opportunistic:** at the start of any session that reads from a connector, do the cheap version. Verify the capabilities that session is about to use, and update their rows. Skip the nudge logic entirely.
- **On demand:** "what are you connected to", "check my connections", "why didn't you see that meeting".

## What this behaviour is for

The system needs to know the difference between three things that all look identical in the output:

1. Nothing happened.
2. Something happened and the tool that would have caught it is not connected.
3. Something happened, the tool is connected, and it quietly stopped working three weeks ago.

The third one is the dangerous one. The leader still thinks the sweep is running.

## Reading order

1. `{{MANUAL}}`.
2. `connections.md`. This is both the input and the output.
3. `about-me.md` and `my-work.md`, only far enough to judge whether a gap actually matters to this leader.
4. Yesterday's calendar, if the Transcripts trigger needs evaluating.

---

## Job A: Notice what changed

{{#claude}}
Probe every capability read-only, the same way `onboarding` does. Then sort every row into exactly one of four buckets.
{{/claude}}
{{#chatgpt}}
ChatGPT cannot enumerate its own connectors, so probe by use rather than by listing. Try one cheap read against each capability the registry claims is connected, and ask the leader once about anything the registry has as `missing`. Then sort every row into exactly one of four buckets.
{{/chatgpt}}

### 1. Newly connected

Registry says `missing`, probe says it responds.

- Update the row: status `connected`, provider, today's date.
- Append an **activation offer** to the queue in `connections.md`.
- Log the change.

The offer names the behaviour, not the tool:

```
[offer] 2026-07-24 | Transcripts | Otter | daily-transcript-sweep | status: pending
```

Which the morning brief renders as:

> You connected Otter. Want me to turn on the daily transcript sweep, so tomorrow's meetings come back as action items?

**Never turn the behaviour on yourself.** A tool appearing is not consent. It is frequently someone else in the org connecting something, or the leader trying a trial. Offer, wait, log the answer.

If the offer is declined, mark it `declined` and do not re-offer for that provider. If the leader says nothing for three briefs, drop the offer quietly. A pending offer that keeps reappearing is a nag with extra steps.

### 2. Newly disconnected or failing

Registry says `connected`, probe errors or returns nothing when it should return something.

- Update the row: status `failing`, keep the provider, keep the old Last verified date so the leader can see how long it has been.
- Flag it. This one bypasses the nudge gates entirely, because it is not a nudge. It is a fault report.

The line reads like a fault, with the cost attached:

> Otter has not returned a transcript since July 3. Three weeks of meetings did not get swept.

A broken capability is worse than a missing one. A missing one, the leader knows about.

Be careful about one false positive: a tool that returns nothing because nothing happened. If the calendar shows no meetings in the window, an empty transcript list is correct behaviour, not a fault. Check before you flag.

### 3. Still connected

Update Last verified to today. Nothing else. Do not mention it. Do not congratulate anyone. Silence is the correct output for a working system.

### 4. Still missing

Consider a nudge, under Job B. Most weeks the answer is no.

---

## Job B: Decide whether to say anything

A nudge surfaces only when **all three gates pass**. Check them in order and stop at the first failure.

### Gate 1: Cadence

`today - Last nudged >= Nudge cadence`. If Last nudged is empty, the gate passes.

Cadences live in `connections.md`. Defaults: 14 days for Calendar, Email, Transcripts. 21 for Documents. 30 for Chat and Tasks. 45 for CRM.

### Gate 2: Not silenced

`Dismissed` is `no`, and `Snoozed until` is empty or in the past.

Read the leader's words plainly and write the result down:

| The leader says | What you write |
|----------------|---------------|
| "Not now", "later", "remind me sometime" | `Snoozed until` = today + cadence |
| A second "not now" | `Dismissed` = yes |
| "Never", "stop asking", "I don't want that" | `Dismissed` = yes |
| "Ask me in a month" | `Snoozed until` = today + 30 |

Two soft noes are a hard no. Someone who declines twice is not undecided. They are being polite.

### Gate 3: Relevant trigger

Being due is not a reason to speak. There has to be a moment that day where the missing capability would have paid for itself, and you have to be able to name it.

| Capability | Trigger |
|-----------|---------|
| Calendar | The leader asked for a brief or prep and there was no schedule to read |
| Email | External meetings happened and there is no inbox to check for follow-through |
| Documents | A brief had to label something `(not connected)` for a project `my-work.md` lists as a priority |
| Transcripts | Two or more meetings on yesterday's calendar and nothing captured any of them |
| Chat | A commitment surfaced that clearly started in a channel you cannot read |
| Tasks | The commitment ledger has not moved in more than 14 days |
| CRM | Meeting prep for an external party returned no history at all |

No trigger, no nudge, even if it is overdue by a month. This gate is what makes the difference between advice and nagging. The nudge is not "you are missing a tool." It is "here is the specific thing that just cost you, and here is what would have caught it."

### The cap

**At most one capability nudge per morning brief, ever.** If several pass all three gates, surface the highest-value one and hold the rest until their next cadence window.

Value order, high to low: Calendar, Email, Transcripts, Documents, Tasks, CRM, Chat.

A fault report (bucket 2) does not count against this cap, and does not consume the nudge slot.

If you queue both a nudge and an activation offer for the same brief, the offer wins and the nudge holds. Do not write a `Last nudged` date for a nudge that never rendered.

---

## Output

This behaviour writes to files. It does not write to the leader.

1. Updated rows in `connections.md`.
2. Appended activation offers, if any.
3. Appended change-log lines, one per change.
4. At most one queued nudge, with its trigger recorded, for the morning brief to render.

When run on demand by the leader, it may also print a plain status table. That is the one case where it speaks directly, because it was asked a direct question.

## Nudge copy

One line. Name the moment, name the cost, name the tool class, and say when you will stop.

Good:

> You had four meetings yesterday with nothing capturing them. A transcription tool that records where you meet (Grain, Otter, Fathom, Granola) would let me pull the action items automatically. I will not raise this again for two weeks.

Bad:

> I noticed you don't have a transcription tool connected! Connecting one would help me serve you better. Would you like some recommendations?

The first names a real cost the leader felt yesterday and promises to go away. The second is an advertisement.

Always include the "I will not raise this again for [cadence]" clause. It is the part that makes the nudge tolerable, and it is a promise the registry actually keeps.

## What this behaviour must never do

- Connect, authenticate, install, or reconfigure anything.
- Turn on a behaviour because a tool appeared.
- Nudge about a capability marked `Dismissed`.
- Nudge more than once per brief.
- Nudge without a named trigger from that day.
- Speak to the leader directly on a scheduled run. It decides. The morning brief delivers.
- Recommend a specific vendor as the answer. Name two or three, or name the class. Check they cover the platform the leader actually meets on before naming them.

## Worked example of a normal month

- Week 1: everything connected still connected. Registry dates updated. Brief says nothing.
- Week 2: leader connects Fathom. Next brief: "You connected Fathom. Want me to start the daily sweep?" Leader says yes. Sweep turns on, offer marked accepted.
- Week 3: nothing changed. Brief says nothing.
- Week 4: CRM still missing, cadence is due, but no meeting prep came back empty this week. Gate 3 fails. Brief says nothing.

Three of four weeks, silent. That is the intended ratio.
