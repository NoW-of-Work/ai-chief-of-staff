> **Example file, read-only.** Invented leader, invented company. The leader's own files live in the workspace root, not in this folder.

# commitments.md — Open Loop Ledger

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
[Active]    | 2026-03-10 | By me | Denise Okafor (Fairloch Foods) | Confirm a ship date for the Depot Sync multi-depot report | due 2026-03-10 | source: meetings/2026-03-09-fairloch-escalation/notes.md
[Active]    | 2026-03-12 | By me | Hannah Sorbara | Give the Fairloch renewal assumption for the NRR line in the data room | due 2026-03-18 | source: email thread, "NRR line, need your call"
[Active]    | 2026-03-13 | By me | Gord Aylward | Operating model section for the data room, implementation and support cost per customer | due 2026-03-20 | source: meetings/2026-03-13-series-b-prep/notes.md
[Active]    | 2026-03-05 | By me | Yusuf Adeyemi | Decision on the Director of Implementation Delivery offer | due 2026-03-17 | source: email thread, "following up after the panel"
[Active]    | 2026-02-26 | By me | Renée Lachapelle | Decide whether implementation moves out from under Devin Osei | due unknown | source: meetings/2026-02-26-cs-monthly/notes.md
[Awaiting]  | 2026-03-04 | To me | Devin Osei | Re-sequenced go-live plan for the 11 waiting customers | due 2026-03-11 | source: meetings/2026-03-04-implementation-review/notes.md
[Awaiting]  | 2026-03-11 | To me | Denise Okafor (Fairloch Foods) | Written confirmation of what her board needs by March 31 | due 2026-03-16 | source: email thread, "renewal timing"
[Awaiting]  | 2026-02-20 | To me | Alan Whitcombe (Braemar Provisions) | Signed change order for the second depot | due unknown | source: email thread, "depot two paperwork"
[To verify] | 2026-03-09 | By me | Denise Okafor (Fairloch Foods) | A service credit for the December outage may have been offered. The wording in the notes is ambiguous. | source: meetings/2026-03-09-fairloch-escalation/notes.md
```

---

## Released

Dropped by mutual agreement or no longer relevant. Kept, never deleted, so the trail survives.

```
[Released] | 2026-01-15 opened | 2026-03-02 released | By me | Gord Aylward | Run a pricing model review before the raise | reason: pricing settled on January 22, the review no longer changes the deck
[Released] | 2026-02-05 opened | 2026-02-27 released | By me | Renée Lachapelle | Rebuild the support ticket taxonomy this quarter | reason: parked to July 1, it does not move net revenue retention this quarter
```

---

## Closed (this quarter)

```
[Closed] | 2026-02-11 opened | 2026-02-27 closed | By me | Hannah Sorbara | Cost-to-serve model for the three largest customers | source: drive, "Larkfield cost to serve, February"
[Closed] | 2026-02-18 opened | 2026-03-03 closed | To me | Wes Kilbride (Ravenscliff Partners) | Board sign-off on the go-live metric definition | source: email thread, "metric definitions, signed off"
[Closed] | 2026-03-02 opened | 2026-03-06 closed | By me | Renée Lachapelle | Approve the Fairloch escalation plan | source: meetings/2026-03-06-fairloch-plan/notes.md
[Closed] | 2026-02-24 opened | 2026-03-09 closed | To me | Devin Osei | Root-cause note on why go-live averages 74 days | source: drive, "Implementation cycle time, root cause"
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

As of 2026-03-17 that scan returns five `Active` by me, three `Awaiting` to me, and three stale: Alan Whitcombe at 25 days, Renée at 19 days, Devin at 13 days.
