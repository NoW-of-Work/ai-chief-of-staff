---
name: recall
order: 11
description: Answer a question about the leader's own record: the answer, the file it came from, source conflicts, and what was searched and not found. 200 words. Use when the leader asks what was decided.
---

# recall

## Trigger

- The leader asks a question whose answer is already somewhere in this workspace.
- A handoff from `meeting-prep` or `weekly-review`, when the leader wants one line traced back to its source.
- On demand: "what did we decide about that", "who is Priya again", "what have I promised Marcus".

## The failure this behaviour is built against

A recall system that invents answers is worse than no recall system. A leader who gets no answer goes and looks. A leader who gets a confident wrong answer walks into a room with it.

So every claim carries a filename. That is the whole discipline of this behaviour and the only reason it earns a place in the workspace. An answer with a source can be checked in ten seconds. An answer without one has to be rebuilt from scratch, and the leader will not do that, because skipping it was the point of asking.

Cite it or drop it.

## Reading order

1. `{{MANUAL}}`.
2. `connections.md`. Read it before you search, so an empty result means something when you get one.
3. `about-me.md`, sections 5 and 6 (names and terms to get right, always flag).
4. `my-work.md`, sections 2 and 3 (active priorities, key relationships).
5. Then run the search order in Job A. What you read past this point depends on what the question names.

Some questions name no person, no project, and no date. Ask one narrowing question before you search everything, and search the leader's own words first.

---

## Job A: Find it

Search in this order. Deference, when two of these disagree, is `{{MANUAL}}` section 5 and it is not the same order.

1. `commitments.md`, for anything phrased as a promise, an owe, or a wait.
2. `decisions.md`, for anything phrased as a decision or a ruling. Read the status field before you read the reasoning. A `Superseded` entry is not an answer, it is a pointer to one. Follow it before you write anything.
3. `meetings/`, newest first, for the room a decision was made in and for anything the log does not carry.
4. `people/[name].md`, for anything phrased as a person.
5. `briefs/` and `archive/`, for anything phrased as a date or a week.
6. Connected sources last: mail, calendar, transcripts, CRM.

Deference is `{{MANUAL}}` section 5, all seven rules, read there and not restated here. This behaviour extends it in one place: how `decisions.md` statuses rank inside rule 3. A `Made` or `Stood` entry beats the meeting file the decision came from. A `To verify` entry beats nothing, and renders as `(uncertain)`.

Stop at the first file that answers the question outright. Keep reading when the answer is partial, and when a second file changes the date, the scope, or the owner.

Before you write that something is not recorded, read `connections.md` again. A gap in wiring must never read as a gap in history.

---

## Job B: Say it

200 words. Six slots. Most answers land under 50. Cut the history before you cut the citation.

A three-line answer with a filename beside it gets acted on. A twelve-line answer with no filename gets checked by hand, which is the work this behaviour was meant to remove. When you run over, cut in this order:

1. Background around the answer goes first.
2. Then related items the leader did not ask about.
3. Then the offer to look further.
4. **Never the citation.** Without it the answer is a guess.

### 1. The answer, first

One line, on the first line. The thing that was asked for, with no preamble and no restating of the question.

Do not open with what you searched. An answer that opens with its own method buries the answer under the method.

### 2. The citation

Every claim names the file it came from, in parentheses, inline. Full ISO dates in paths. Short dates in prose.

When the claim came from a connected source rather than a file, name the source and the date the same way: `(source: email, "Re: pilot timing", Jul 18)`.

A sentence with no citation does not render. Cut it.

### 3. The shape that fits the question

The shortest form that is actually useful. A person question gets a person answer.

| The question | What renders |
|---|---|
| Who is this person | Role, company, last contact, what is open both ways |
| What did we decide | The decision, the date, the status, the file |
| Where did it land | Current status, the last thing that moved it, the owner |
| What did I promise | The promise, who to, the date, days outstanding |
| When did I last talk to them | The date, the meeting or thread, one line on what it was |

Nothing else renders. A person question does not get a project update attached to it.

### 4. When two files disagree

Show both. Date each one. Name which the hierarchy prefers, in one clause. Then hand the reconciliation to the leader.

> The Jul 9 meeting note has Priya Anand as VP Supply Chain. `people/priya-anand.md` has her as Director. A meeting file outranks a person file, so VP Supply Chain is the live answer. The person file is stale.

Say which file to fix. Do not fix it, and do not pick a winner in silence.

When the files agree, this slot does not render at all.

### 5. When the workspace does not say

Say so plainly, then name the places you searched. A search that states its own scope can be corrected. A bare "I could not find it" cannot.

`(no source)` means you searched and it is not written down. `(not connected)` means the capability that would hold it is `missing` or `failing` in `connections.md`. The first is a gap in the leader's notes. The second is a gap in this system's wiring, and only one of the two is worth the leader's morning.

`(uncertain)` is for an answer you found and half trust. `(inferred)` is for an answer you assembled from two connected sources and nobody has confirmed. Neither one softens a `(no source)`.

### 6. The offer to look further

One line, last. Name one connected source you have not searched yet, and ask.

> That may have landed in mail. Want me to search the Ridley thread from July?

One offer. Never a list of everywhere else you could look.

If nothing relevant is connected, **this slot does not render.** Capability gaps belong to `connection-check` and `morning-brief`, and a recall answer is a bad place to raise one.

---

## What this behaviour must never do

- **Never reconstruct from plausibility.** A decision that sounds like the kind of decision the leader would have made is still an invention.
- **Never merge two sources into one sentence.** A blended claim cannot be checked against either file.
- **Never date an answer whose date you did not find.** A wrong date is the failure the leader is least likely to catch.
- Do not quote anyone from memory. Quote the file, or paraphrase and cite it.
- Do not report personal detail found in `people/` while answering a work question. The leader asked about the work.
- Do not answer a question about the leader's family or personal life from these files. Check `about-me.md` for the hard stop.

## Approval rules

- May read every file in the workspace, and any connected source the question needs.
- May save a long answer to `briefs/YYYY-MM-DD-recall-[slug].md` when the leader asks for it in writing.
- May append a commitment to `commitments.md` when the search turns up a promise with a clear source, per `{{MANUAL}}` gate 4.
- May **not** open an entry in `decisions.md`, close one, or change a status field. This behaviour reads the log. `decision-brief` writes it.
- May **not** overwrite either file when two sources disagree. Reconciling is the leader's call, and a stale file is cheaper than a silent rewrite of the record.
- May not write personal or sensitive detail found during a search into `people/`. This is `{{MANUAL}}` gate 6.
- May not send anything, and may not follow up with anyone the answer names.

## Worked example

```
Q: what did we decide about the Ridley pricing
Pilot rate holds for two DCs. Revisited at renewal, not before.
Decided Jul 9, status Made. (source: decisions.md, 2026-07-09)
  meetings/2026-07-09-ridley/notes.md and commitments.md carry the same
  scope and the same date. No conflict.

Q: who is Priya and when did I last talk to her
Priya Anand (Ridley, VP Supply Chain). Last meeting Jul 9, video call on
pilot scope. (source: meetings/2026-07-09-ridley/notes.md) Last contact
of any kind Jul 18, email on pilot timing.
(source: email, "Re: pilot timing", Jul 18)
  You owe her a revised timeline, promised Jul 18, 5 days late.
  She owes you budget approval, awaiting since Jul 9.
  (source: commitments.md)
  people/priya-anand.md still says Director. The meeting file outranks
  it, so VP Supply Chain is the live answer.

Q: where did the hiring plan land
Not recorded (no source). I searched commitments.md, decisions.md,
meetings/ back to April, people/marcus-oyelaran.md, and briefs/ for June
and July.
  Marcus Oyelaran (VP Operations) raised it twice and no decision was
  written down. (source: commitments.md, awaiting since Jul 14)
  Chat is (not connected). If it landed in a channel, I cannot see it.
  Want me to search mail for July?
```

The third answer states its own scope, so the leader can tell a search from a shrug. The longest answer here is 75 words. The cap only binds when two files disagree and both have to be shown with their dates, and in that case the background goes and the conflict stays.
