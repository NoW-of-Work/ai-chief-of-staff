---
name: meeting-prep
order: 2
description: Prep for a specific meeting: who, why, what happened last time, what is open between you both ways, three questions worth asking, and the risks. 300 words. Use before a meeting that matters.
---

# meeting-prep

## Trigger

- Before a meeting the leader flagged, or one involving anyone in the key-relationships table in `my-work.md`.
- When the morning brief finds a high-stakes meeting with no prep and the leader says yes.
- On demand: "prep me for the 11:00", "what do I need to know before I talk to Priya".

## Reading order

1. `{{MANUAL}}`.
2. `connections.md`. Know before you start whether you can read mail, documents, past transcripts, and CRM history. It changes what "I found nothing" means.
3. `about-me.md`, sections 5 and 6 (names and terms to get right, always flag).
4. `my-work.md`, section 3 (key relationships) and section 2 (priorities this meeting might touch).
5. `commitments.md`, filtered to everyone in the room.
6. `people/[name].md` for each attendee, if it exists.
7. `meetings/` for the last meeting with these people.
8. The calendar entry itself. Then recent mail with the attendees. Then CRM, if connected.

---

## Structure

300 words. Six slots. Cut background before you cut questions.

### 1. The meeting

Time, attendees with roles, and the format (call, in person, group). One line.

If a role is a guess, label it `(uncertain)`. Getting someone's title wrong out loud is expensive.

### 2. Why this is happening

One or two sentences. The actual purpose, not the calendar title. Pull from the invite body, the thread that created it, or the last meeting's follow-up.

If you cannot tell, say `(no source)` and say what you think it is likely about. Do not dress up a guess as a fact.

### 3. Last interaction

What happened last time and what was decided. Date it. Cite the file.

If there is no prior meeting on record, say so. If there is no prior meeting on record **because there is no transcript or notes capability connected**, say that instead, with `(not connected)`. Those are different problems and only one of them is the leader's.

### 4. Open between you

From `commitments.md`, both directions:

- What the leader owes them, and how overdue it is.
- What they owe the leader, and how long it has been.

This is the highest-value slot in the whole brief. The leader walking into a room knowing they still owe someone a redline from two weeks ago is worth more than any amount of background.

### 5. Three questions

Exactly three. Questions that move the meeting forward, not questions that show the leader did reading. Grounded in the open loops and the current priority, not generic.

A good question here is one the leader would not have thought to ask, and could not have asked without the sources you read.

### 6. Risks

What could go wrong, in one or two lines. Something unresolved, someone who was unhappy last time, a number that will get asked for and does not exist yet, a decision the leader is not ready to make.

Include what the leader should **not** commit to in this meeting, if `my-work.md` section 5 makes that obvious.

---

## Rules

- Never invent what someone said. If it is not in the notes, transcript, or mail, it did not get said.
- Never invent a role, a company, or a relationship.
- Never guess a number.
- Use the correct spelling of every name. Check `about-me.md` section 5 first. This is the single most visible thing you can get wrong.
- If the meeting is personal or family, do not prep it. Check `about-me.md` for the hard stop.

## Approval rules

- May create a stub `people/[name].md` for an attendee with no file, containing role and meeting history only.
- May save prep to `meetings/YYYY-MM-DD-[slug]/prep.md`.
- May not write personal or sensitive detail about an attendee, in any file, without approval in the same session. This is `{{MANUAL}}` gate 6. In prep specifically, the answer should almost always be no. Work facts are enough.
- May not send anything to anyone in the meeting.

## Worked example

```
11:00, Priya Anand (Ridley, VP Supply Chain), video call, 30 min.

WHY
Follow-up on the pilot scope. She asked for revised timing on Jul 18 and you
said you would come back with dates. (source: email, "Re: pilot timing")

LAST TIME
Jul 9. Agreed the pilot covers two DCs, not four. She raised budget approval
timing and it was left open. (source: meetings/2026-07-09-ridley/notes.md)

OPEN BETWEEN YOU
  You owe her: revised timeline. Promised Jul 18, now 5 days late.
  She owes you: budget approval confirmation. Awaiting since Jul 9.

THREE QUESTIONS
1. Has the budget cleared, or is that still with finance?
2. If the two DCs go well, who decides whether it extends?
3. What would make this a failure in her eyes, in the first 30 days?

RISKS
The timeline is late and she will notice. Lead with it.
Do not agree to four DCs. my-work.md says scope creep on pilots is the thing
you are trying to stop this quarter.
```
