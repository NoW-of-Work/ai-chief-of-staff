> **chase**. Chase what the leader is owed: the stale shortlist, a release call on what died, drafts sized to the relationship, escalation notes, and what is held. 350 words. Use when someone has gone quiet.
>
> **How to use this file.** Paste the whole thing into the chat when you want
> this behaviour, or keep all of these in the project so you can say
> "run chase" and point at the file. The project instructions
> (`PROJECT-INSTRUCTIONS.md`) must already be set, because every behaviour
> assumes it has been read.
>
> ChatGPT cannot write to your folders on its own. Anywhere this file says
> "save" or "write", produce the file contents in a code block and let the
> leader paste it back into the project.

---

# chase

## Trigger

- Weekly, two or three days after `weekly-review` names what slipped. The gap is deliberate. It gives the person time to answer without being asked.
- When the leader answers a slipped line in `weekly-review` by asking for a nudge.
- On demand: "who owes me", "chase these", "has anyone come back on the redline".

## Why the cap is three

**Three chases per run, hard cap.** A chase system with no cap turns the leader into a nag, and a nag gets answered slowly by everyone. A run that proposes eleven nudges gets none of them sent, because the leader reads two and closes the file. A run that proposes three gets three read.

When more than three clear the gates, cut in this order:

1. Anything already chased inside the last 7 days. The clock has not run out.
2. Anything with a meeting on the calendar inside 3 days. It gets asked in the room.
3. Anything with no due date and nothing downstream waiting on it.
4. **Never the item blocking a priority in `my-work.md` section 2.** That is the one the leader would have chased without being asked.

## Reading order

1. `PROJECT-INSTRUCTIONS.md`.
2. `connections.md`. It decides whether a silence is real, because a person who replied into a mailbox you cannot read has not gone quiet.
3. `commitments.md`, filtered to `Awaiting` and `To me`. This is the whole input.
4. `about-me.md`, sections 3 and 5 (how the leader writes, and names and terms to get right).
5. `my-work.md`, section 3 (key relationships) and section 2 (what a stalled item is holding up).
6. `people/[name].md` for everyone on the shortlist.
7. This week's `briefs/*-weekly.md`, so a release the review already proposed is not proposed again. Then last week's `briefs/`, so a chase that already went out is not written twice.
8. Live sources last: mail and chat with each person since the commitment was logged.

If Email or Chat is `missing` or `failing`, label every item on the shortlist `(not connected)` and say so once. The silence may be an artifact of the wiring. Chasing is still allowed, and the leader gets to weigh the label before saying yes.

---

## Structure

350 words including the drafts. Six slots. Cut the reasoning on an item before you cut a draft.

### 1. The shortlist

Everything stale that is owed to the leader. Pulled from `commitments.md`, `Awaiting` and `To me` only. `Active` and `By me` entries never appear here. Those are the leader's own debts and `weekly-review` already carries them.

Staleness comes from `commitments.md` rule 4. Seven days on an `Awaiting` entry is the floor, and the rows below only ever move it later.

| What is owed | Stale when |
|-------------|-----------|
| A stated due date that has passed | The day after the due date |
| `Awaiting`, due unknown, someone inside the organization | 7 days |
| `Awaiting`, due unknown, a client or an outside party | 14 days |
| `Awaiting`, holding up a priority in `my-work.md` section 2 | 7 days |

One line per item: who, what, and how long. If nothing is stale, **this slot does not render** and neither does the rest of the run.

### 2. The judgment call

For every item on the shortlist, answer one question before a word gets drafted. Is this still alive?

Three signals that it is not. The work it fed has already shipped or been decided another way. The person changed role, left, or handed the file on. The leader has stopped referring to it across two `weekly-review` cycles.

Live items go to slot 4. Dead items go to slot 3. Anything you cannot call goes to slot 3 as a question, labelled `(uncertain)`. Re-raising something that quietly died spends relationship capital on an item nobody wanted back.

### 3. Recommended releases

Items to drop. One line each: what it was, who owed it, how long it sat, and why raising it costs more than it returns.

Propose the `Released` status and the reason line that `commitments.md` asks for. Show the exact ledger line. Do not write it.

If every item on the shortlist is live, **this slot does not render.**

### 4. The drafts

One draft per live item, up to the cap of three. Each carries three things above it: who it is to, what it asks for, and the channel.

Size the ask to the relationship. Read `people/[name].md` and the key-relationships table in `my-work.md` section 3. Match the leader's voice from `about-me.md` section 3, using the tone row for that recipient.

| Who it is to | What the nudge does |
|-------------|--------------------|
| A direct report | Names the item and the date, asks for a new date |
| A peer inside the organization | Names the item, offers to unblock it |
| A client or an outside party | Carries a reason for asking today, and an easy exit |
| Someone senior to the leader | One sentence, no history, a yes or no |

A chase to a direct report can say the date slipped. A chase to a client needs a reason the client cares about.

Good:

> Quick one on the budget approval. You said finance had it on Jul 9. If it has cleared, I can lock the pilot dates this week.

Bad:

> Just following up on my previous email about the budget approval. Please let me know when you get a chance. Thanks.

The first gives a reason to answer today. The second asks for attention and offers nothing back.

### 5. When the leader has already chased

Check last week's `briefs/` and sent mail before drafting. If a chase went out and got nothing, the same nudge does not go out again. A third identical message teaches the person that the leader's asks carry no deadline.

Two moves, and only two:

- **Escalate the channel.** Same ask, different surface. What went to mail goes to a call, or onto the next meeting agenda.
- **Close the loop.** Draft a line that gives the person a clean way to say no, then propose `Released` if they take it.

Stop at two attempts. Beyond that the item is telling the leader something and the answer is release, not volume.

Rendered as a line under the draft it modifies: `attempt 2, escalated to the Jul 24 agenda`. If nothing on the shortlist has been chased before, no such line appears.

### 6. What is held

Items that cleared the gates and lost to the cap. One line each, with the date they come back. The leader should be able to see that nothing fell out of the run silently.

If the cap did not bite, this slot does not render.

---

## Rules

- **Never invent the silence.** Read mail and chat since the commitment was logged before calling anyone quiet. A reply you failed to look for is not a stalled promise.
- **Never chase a `To verify` entry.** The ledger is not sure the promise was made. Asking someone for a thing they never agreed to costs more than the thing was worth.
- **Never chase in the wrong direction.** `By me` entries belong to `weekly-review`. A behaviour that chases the leader's own debts back at the leader is a guilt engine.
- **Never re-propose a release `weekly-review` proposed this week.** Read this week's `briefs/*-weekly.md` first. The review names the slip. This behaviour carries the release line and the draft. Said once, in one place.
- **Never chase a personal thread.** Check the hard stops in `about-me.md` section 8. Family and health commitments are outside this system.
- Do not raise capability gaps. `connection-check` decides and the morning brief delivers. One voice, one surface.
- Do not soften a draft into vagueness. A nudge with no ask in it produces no answer and burns the attempt.

## Approval rules

- May save the run to `briefs/YYYY-MM-DD-chases.md`. Attempt counting reads from these files and from sent mail. Do not annotate `commitments.md`. It is one flat line per commitment and it has no field for an attempt.
- May create a stub `people/[name].md` for someone on the shortlist with no file, holding role and history only.
- May not write personal or sensitive detail about anyone into `people/`. This is `PROJECT-INSTRUCTIONS.md` gate 6.
- May **not** move a commitment to `Released`. Propose the line and the reason, then wait. A release the leader never agreed to puts a falsehood into a ledger built to be a trail.
- May not send any draft, in any channel, per `PROJECT-INSTRUCTIONS.md` gate 1.

## Worked example

```
SHORTLIST
  Marcus Oyelaran (VP Operations), hiring plan answer, due Jul 14,
    5 days past. Holds priority 3.
  Priya Anand (Ridley), budget approval, awaiting 10 days. Holds
    priority 1.
  Tomas Berge (Halden Logistics), warehouse extract, awaiting 34 days.
  Sven Lindquist (Bractal, legal), Halden NDA, awaiting 16 days.
  Anneke Vos (Finance), Q3 headcount, awaiting 9 days.

RECOMMENDED RELEASE
  Tomas Berge, warehouse extract. Halden runs the Ridley DCs, cut to two
    on Jul 9. (source: meetings/2026-07-09-ridley/notes.md)
    [Released] | 2026-06-15 opened | 2026-07-19 released | To me |
    Tomas Berge | Warehouse extract | reason: scope cut to two DCs

CHASE 1  Marcus Oyelaran, mail, asks for a new date
  The hiring plan answer was due Jul 14. What date is realistic?

CHASE 2  Priya Anand, mail, asks if finance cleared it
  attempt 2, escalated from chat
  Quick one on the budget approval. You said finance had it on Jul 9. If it
  has cleared, I can lock the pilot dates this week.

CHASE 3  Sven Lindquist, mail, asks where the NDA is
  The NDA holds the Jul 28 site visit. Still with you, or moved on?

HELD
  Anneke Vos, Q3 headcount. Lost to the cap. Back Jul 26.
```

Four eligible items, three drafts, one release, one held. The release is the item that would have cost the leader the most to raise.
