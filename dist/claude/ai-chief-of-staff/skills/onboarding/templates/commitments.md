# commitments.md — Open Loop Ledger

> **Template note.** This file tracks promises with people attached, not private to-dos. A task is something only the leader is responsible for. A commitment has another person on the hook — either the leader owes them something or they owe the leader something.
>
> The AI Chief of Staff appends entries here when a meeting transcript, email, or note clearly supports the promise. If the source is unclear, the AI flags it as `To verify` instead of inventing it.
>
> Keep the format flat. One line per commitment. The leader skims this in 30 seconds at the start of every working day.

---

## Status taxonomy

- **Active** — open, on the clock, action required.
- **Awaiting** — owed to the leader, ball in someone else's court.
- **Closed** — fulfilled, with a source as evidence (email sent, deliverable shipped, decision made).
- **Released** — dropped by mutual agreement or no longer relevant.
- **To verify** — the AI Chief of Staff is uncertain a commitment was actually made. Needs leader review.

---

## Direction

- **By me** — the leader owes someone something.
- **To me** — someone owes the leader something.

---

## Format

One entry per line. Pipe-separated. The AI Chief of Staff writes new entries in this format.

One line per open entry:

```
[Status] | YYYY-MM-DD | [By me / To me] | [Person or group] | [What] | due [YYYY-MM-DD or unknown] | source: [file path or app reference]
```

Closed entries carry a second date, so the ledger shows how long the loop was open. Released entries carry a release date and a reason in place of a source, because nothing was delivered:

```
[Closed]   | YYYY-MM-DD opened | YYYY-MM-DD closed   | [By me / To me] | [Person] | [What] | source: [evidence path]
[Released] | YYYY-MM-DD opened | YYYY-MM-DD released | [By me / To me] | [Person] | [What] | reason: [why it was dropped]
```

---

## Active commitments

```
[Active] | YYYY-MM-DD | By me | [Person] | [What was promised] | due [YYYY-MM-DD] | source: meetings/YYYY-MM-DD-[meeting-name]/notes.md
[Active] | YYYY-MM-DD | By me | [Person] | [What was promised] | due unknown | source: email thread, [subject]
[Awaiting] | YYYY-MM-DD | To me | [Person] | [What they owe] | due [YYYY-MM-DD] | source: meetings/YYYY-MM-DD-[meeting-name]/notes.md
[To verify] | YYYY-MM-DD | By me | [Person] | [Possible commitment to clarify] | source: meetings/YYYY-MM-DD-[meeting-name]/transcript.md
```

---

## Released

Dropped by mutual agreement or no longer relevant. Kept, never deleted, so the trail survives.

```
[Released] | YYYY-MM-DD opened | YYYY-MM-DD released | By me | [Person] | [What was promised] | reason: [why it was dropped]
```

---

## Closed (this quarter)

```
[Closed] | YYYY-MM-DD opened | YYYY-MM-DD closed | By me | [Person] | [What was promised] | source: [evidence path]
```

Archive entries older than 90 days to `archive/commitments-[YYYY]-Q[N].md` quarterly.

---

## Rules the AI Chief of Staff must follow

1. **No commitment without a source.** If the AI cannot point to a file, transcript, or email, it does not write the commitment. It writes a `[To verify]` entry instead.
2. **No marking `Closed` without evidence.** The source field must name what proves the commitment was met: the sent mail, the shipped file, the decision in the notes. The leader saying "that's done" is a valid source, recorded as such, with the date.
3. **No inventing due dates.** If a due date was not stated, write `due unknown`.
4. **Surface stale commitments.** Anything `Active` for more than 14 days, or `Awaiting` for more than 7 days, gets flagged in the weekly review.
5. **Never delete an entry.** Move to `Released` or `Closed`. The ledger keeps a trail.

---

## Weekly review

Every Monday the AI Chief of Staff scans this file and produces:

- Count of `Active` (split by `By me` / `To me`).
- Anything stale (see rule 4).
- Anything due in the next 7 days.
- Anything that has changed status in the last 7 days, with the source for the change.
