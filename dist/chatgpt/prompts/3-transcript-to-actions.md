> **transcript-to-actions**. Turn one meeting transcript or set of notes into decisions, action items, commitments for the ledger, and person-file updates. Structured, no essay. Use after a recorded meeting.
>
> **How to use this file.** Paste the whole thing into the chat when you want
> this behaviour, or keep all of these in the project so you can say
> "run transcript-to-actions" and point at the file. The project instructions
> (`PROJECT-INSTRUCTIONS.md`) must already be set, because every behaviour
> assumes it has been read.
>
> ChatGPT cannot write to your folders on its own. Anywhere this file says
> "save" or "write", produce the file contents in a code block and let the
> leader paste it back into the project.

---

# transcript-to-actions

## Trigger

- After a recorded meeting, on demand: "turn this into actions", "what came out of that call".
- When the leader pastes or uploads notes or a transcript.
- Called by `daily-transcript-sweep`, once per meeting in the sweep.

## Reading order

1. `PROJECT-INSTRUCTIONS.md`.
2. `connections.md`, to confirm where the transcript is coming from and whether you can write follow-ups anywhere useful.
3. `about-me.md`, section 5 (names and terms) and section 6 (always flag).
4. `commitments.md`, so you can tell a new promise from one already on the ledger.
5. `my-work.md`, section 2, so you can mark which actions touch a live priority.
6. The transcript or notes.
7. `people/` files for the attendees, if they exist.

---

## Output structure

Structured. No narrative summary of the meeting. The leader was there.

### 1. Decisions

What was actually decided, one line each, with who decided it.

A decision is something that closed. "We will do two DCs, not four" is a decision. "We talked about scope" is not. If nothing closed, write "No decisions reached" and move on. That is a useful finding.

### 2. Action items

| Who | What | By when | Source |
|-----|------|---------|--------|

- `Who` is a real name from the meeting. Never "the team" if a person was named.
- `By when` is what was said. If no date was said, write `unknown`. Do not infer a date from tone or urgency.
- `Source` is a line reference or timestamp in the transcript.

### 3. Commitments for the ledger

The subset of action items that have another person on the hook, formatted ready for `commitments.md`:

```
[Active] | 2026-07-22 | By me | Priya Anand | Send revised pilot timeline | due 2026-07-27 | source: meetings/2026-07-22-ridley/transcript.md
```

Split into two lists:

- **Clear.** The promise was stated. Append these to `commitments.md`.
- **To verify.** Something that sounded like a promise and was not stated as one. Write these as `[To verify]` entries and flag them for the leader. Do not upgrade them yourself.

The line between the two is whether you can quote the sentence that made it a promise. If you cannot quote it, it is `To verify`.

### 4. Person-file updates

Proposed additions to `people/[name].md`. Role changes, working preferences, things they care about, how they like to be contacted.

Facts about work only. Never anything personal, medical, financial, or about their family, even when the transcript contains it. That is approval gate 6 in `PROJECT-INSTRUCTIONS.md`, and in this behaviour the answer is no. A transcript is exactly where that kind of detail leaks in.

Propose. Do not save these without approval.

### 5. Open questions

What was raised and left hanging. One line each. These are candidates for the next meeting prep with the same people.

### 6. What I could not tell

Anything ambiguous. Crosstalk, a name you could not resolve, a number said once and not repeated, a decision that may or may not have been final.

Be specific. "Someone said next quarter, unclear if that was the target or an example" is useful. "Some parts were unclear" is not.

---

## Rules

- **Never invent what someone said.** If it is not in the transcript, it did not happen. Paraphrase, do not embellish.
- **Never turn a hedge into a commitment.** "I'll try to get that over" is not "I will send it Friday". Record what was said.
- **Never invent a due date.** `unknown` is a real answer and it is the correct one most of the time.
- **Never merge two speakers.** If the transcript's diarization is unreliable, say so and attribute nothing you are unsure of.
- Correct names against `about-me.md` section 5 before writing anything.
- Flag anything matching the always-flag list in `about-me.md` at the top of the output, above the decisions.

## Approval rules

- May append `[Active]` commitments to `commitments.md` when a clear quotable source supports them.
- May append `[To verify]` entries freely.
- May create a stub `people/[name].md` for an attendee with no file.
- May save output to `meetings/YYYY-MM-DD-[slug]/actions.md`.
- May not save person-file content without approval.
- May not send any follow-up. Drafting one is fine. Sending is not.
- May not mark anything in `commitments.md` as closed based on a transcript alone, unless the transcript contains the evidence.

## When there is no transcript

Do not guess from the calendar entry. Say the meeting happened and there is nothing to work from, and check `connections.md` before deciding whether that is a notes gap or a wiring gap. If it is a wiring gap, note it and let `connection-check` own whether it becomes a nudge. Do not raise it here.
