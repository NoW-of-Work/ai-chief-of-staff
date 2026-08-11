---
name: inbox-triage
order: 8
description: Mail since the last pass, cut to what needs a person: decisions, drafted replies, promises in both directions, and a count of what was left alone. 350 words. Use when the inbox has run ahead.
---

# inbox-triage

## Trigger

- Scheduled twice on a working day, once before the morning brief and once an hour before the hard stop in `about-me.md`.
- When `end-of-day-close` needs today's new commitments and no pass has run since morning.
- On demand: "what's in my inbox", "anything I need to answer", "triage my mail".

The first pass feeds the morning brief. Anything it appends to `commitments.md`, and any draft it saves to `briefs/`, is the brief's to render in its open-loops and drafts-waiting slots. Do not hand the leader the same decision twice in one morning. The afternoon pass speaks for itself, because nothing renders after it.

## Before anything else: can you see the inbox

Read the `Email` row in `connections.md` first.

| Status | What this behaviour does |
|--------|--------------------------|
| `connected` | Run the pass. |
| `missing` | Stop. On demand, say one honest line. On a scheduled run, say nothing. |
| `failing` | Stop. Say the line, name the last verified date, and log it in `connections.md`. |
| `unknown` | Stop. Say that `onboarding` has not been run. |

{{#claude}}
Probe Email read-only before trusting the row. A registry written last week is a claim about the past.
{{/claude}}
{{#chatgpt}}
Probe Email with one cheap read before trusting the row, because the connector list cannot be enumerated directly. A registry written last week is a claim about the past.
{{/chatgpt}}

The honest line is one sentence and it says which of the two things happened:

> Email is not connected. I cannot see the inbox, so I cannot tell you it is empty.

An empty inbox and a blind system produce the same silence. Only one of them is good news. This is the failure this check exists to stop, and it is the one the leader would never catch on their own.

## Reading order

1. `{{MANUAL}}`.
2. `connections.md`. Per above, it decides whether nothing found means an empty inbox or a blind spot.
3. `about-me.md`, section 3 (how the leader writes, and the tone row for each kind of recipient).
4. `about-me.md`, sections 6 and 8 (always flag, and the hard stops that keep mail out of this pass entirely).
5. `my-work.md`, sections 2 and 3 (active priorities, key relationships).
6. `commitments.md`, so a promise already in the ledger is not written twice.
7. The timestamp of the last pass. On the afternoon run, this morning's brief in `briefs/` as well, so a decision the brief already raised is not raised again six hours later.
8. The inbox itself, from the last pass forward.

If there is no record of a last pass, read the last 24 hours and say so in one clause. Do not read a week of mail and hand it over as new.

---

## Structure

350 words. Six slots. Cut the counts before you cut the decisions.

A 250-word pass that names three decisions gets acted on before lunch. A 1,200-word pass that names forty messages is the inbox again, with extra steps. The second one feels thorough and does nothing. When you run over, cut in this order:

1. The left-alone count goes first. It is reassurance, and reassurance is not work.
2. Then the waiting-on-them lines. The ledger already holds those.
3. Then background on the reply-only items. The draft carries the context.
4. **Never the decisions.** They are the only thing here that cannot happen without the leader.

Drafts sit outside the word cap and carry two limits of their own: five drafts, 120 words each. Render the slots in this order. A slot with nothing in it does not render.

### 1. Decide

Mail where the leader has to choose, and nobody else can. Two or three lines each: who, what the choice is, and the date it stops being a choice.

Name the options the mail names. Do not invent a third option nobody offered. If the deadline is implied rather than stated, label it `(inferred)`.

Anything matching `about-me.md` section 6 lands here first, even when the decision is small. That list exists because those senders get missed.

Cap this slot at four. If more than four real decisions arrived since the last pass, that is itself the finding. Say it in one line. If nothing needs a decision, **this slot does not render.**

### 2. Reply drafted

Mail that needs words back and nothing else. One line naming the sender and the ask, then the draft.

Write every draft in the leader's voice, per `about-me.md` section 3, using the tone row for that recipient. Keep each under 120 words. A draft the leader has to rewrite costs more than no draft at all.

Save each to `briefs/YYYY-MM-DD-draft-[slug].md` and name the file in the line. Drafting is where this behaviour stops. Nothing leaves.

If the reply needs a fact you do not hold, write around the hole and mark it `(needs check)`. Do not fill it with something plausible.

Cap this slot at five. Past five, draft the five where a reply unblocks someone else's work and roll the rest into the count in slot 5. Five drafts get read and sent. Twelve get skimmed and none of them go out.

### 3. Waiting on the leader

Mail carrying a promise the leader made, or is being held to. Sender, what they believe is owed, and since when.

Append each to `commitments.md` as an `[Active]` entry, direction `By me`, with the mail named in the source field. A promise the mail does not clearly support gets written as `[To verify]` instead, per `{{MANUAL}}` gate 4, and gets one line here so the leader can settle it.

Check the ledger before appending. A commitment written twice reads as two promises and gets chased twice.

### 4. Waiting on someone else

The same thing pointed the other way. Something the leader asked for, has not received, and the mail is the evidence.

Append as an `[Awaiting]` entry, direction `To me`.

Render a line here only when something crossed a threshold: `Awaiting` for more than 7 days, or a stated due date now past. Everything else waits for `weekly-review`. Reading the ledger back in full is not triage.

### 5. Left alone

One line. A count, and the classes it breaks into. Never a list.

Replies you did not draft past the slot 2 cap are one of those classes. Count them and say what they are. That is the whole treatment they get here.

> Left 52 alone: 34 newsletters and notifications, 11 threads someone else answered, 7 where you are copied and not asked anything.

The moment this slot becomes a list, the behaviour has rebuilt the inbox and charged the leader for it. Keep it to one line even when the count is large. Especially when the count is large.

### 6. What did not get sorted

Two things live here, and only when they actually happened.

Mail matching a hard stop in `about-me.md` section 8. Personal, family, anything on the never list. Count it, say nothing about its contents, draft nothing for it.

Mail this behaviour could not read: an attachment with no body, a thread whose opening message is missing, a message in a language you cannot follow. Use `(no source)` when the leader's own trail is thin and `(not connected)` when the wiring is short a source. Those are different problems and only one of them is the leader's.

Do not turn `(not connected)` into a nudge. `connection-check` decides that and the morning brief says it. Silence here is the correct output.

---

## What this behaviour must never do

- **Never change the state of a message.** `{{MANUAL}}` gate 12 covers what that means and why.
- **Never send, reply, or forward.** A draft the leader has not read is a message the leader did not write.
- **Never invent a due date, a figure, or a quote from a thread.** If the mail does not say it, it was not said in the mail.
- **Never report an empty inbox you could not see.** Missing and empty look identical on the page.
- Do not draft in the voice of anyone other than the leader. Check `about-me.md` section 8 first.
- Do not summarize a personal or family thread. Count it in slot 6 and move on.
- Do not raise a capability gap. One voice, one surface.

## Approval rules

- May save each reply draft to `briefs/YYYY-MM-DD-draft-[slug].md`.
- May save the pass to `briefs/YYYY-MM-DD-triage-am.md` on the morning run and `briefs/YYYY-MM-DD-triage-pm.md` on the afternoon one. Two passes a day need two filenames, and the afternoon run reads the morning one back.
- May append sourced commitments to `commitments.md` in both directions.
- May write a `[To verify]` entry when a promise looks real and the source will not carry it.
- May update the `Email` row in `connections.md` when a read fails.
- May **not** open a message in a way that changes its state in the mail client. Read-only, always, per `{{MANUAL}}` gate 12.
- May not send, reply, forward, or schedule a send, ever, for any draft in this pass. That is `{{MANUAL}}` gate 1 and no draft is exempt from it.

## Worked example

```
DECIDE
1. Nadia Okonkwo (Halvorsen Foods, CFO) wants the pilot start moved to
   Sep 8 or Sep 22. She needs an answer by Jul 31.
2. Theo Brandt (Calder Logistics, Head of Ops) asks whether procurement
   or ops signs the SOW. Stalled since Jul 15.
3. Halvorsen legal wants the data clause narrowed or dropped. Either
   answer changes the SOW. No date stated.
4. Bea Lindqvist wants the Q4 workshop dates locked or released back to
   the calendar. Room hold expires Jul 29.
  Four is the cap and four arrived. Two more are waiting behind these.

REPLY DRAFTED
  Lucia Ferrante, asking for the workshop headcount.
  (briefs/2026-07-24-draft-ferrante-headcount.md)
  Marek Sowinski, confirming the Aug 6 site visit window.
  (briefs/2026-07-24-draft-sowinski-site-visit.md)

WAITING ON YOU
  Nadia, revised pricing page. Promised Jul 22, now 2 days late.
  (source: email, "Re: pilot pricing") Appended to the ledger.

WAITING ON THEM
  Theo, signed SOW. Awaiting since Jul 11, 13 days.

LEFT ALONE
  Left 52 alone: 34 newsletters and notifications, 11 threads someone
  else answered, 7 where you are copied and not asked anything.

DID NOT SORT
  3 personal threads, per the hard stop.
  1 attachment-only message from Halvorsen, no readable body.
```

Sixty-six messages in, eight things that need you, under 350 words. The count line stayed a count.
