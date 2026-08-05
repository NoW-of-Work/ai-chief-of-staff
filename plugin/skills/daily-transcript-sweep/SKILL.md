---
name: daily-transcript-sweep
description: "Daily pass over yesterday's recorded meetings, turning each into actions and ledger entries unasked. Checks connections.md first and skips quietly if no transcript tool is connected."
---

# daily-transcript-sweep

## Trigger

- Scheduled, once daily, before the morning brief so its output can feed into it.
- On demand: "sweep yesterday", "catch me up on this week's meetings".

## First thing, every run: check the registry

Read the `Transcripts` row in `connections.md` before doing anything else.

| Status | What this behaviour does |
|--------|---------------------|
| `connected` | Run the sweep. |
| `missing` | **Stop. Exit quietly.** Do not error. Do not write anything. Do not mention it. |
| `failing` | Stop. Log it in `connections.md` if not already logged. `connection-check` will raise the fault. |
| `unknown` | Stop. Note that onboarding has not been run. |

This is the whole point of the registry. Without it, this behaviour runs every morning against nothing, fails, and produces noise. With it, it knows the difference between "no meetings were recorded yesterday" and "there is nothing here that could record a meeting."

**Do not nudge from this behaviour.** Not even once, not even gently. If a transcript tool is missing, `connection-check` decides whether that is worth mentioning and the morning brief says it. One voice, one surface. A behaviour that speaks up on its own schedule is how a system becomes annoying.

---

## Reading order

1. `CLAUDE.md`.
2. `connections.md`, per above.
3. Yesterday's calendar, to know what should have been captured.
4. The transcript source, for the same window.
5. `commitments.md`, so existing promises are not duplicated.
6. `about-me.md`, section 6 (always flag).

---

## The sweep

### 1. Reconcile calendar against transcripts

List yesterday's meetings. Match each to a transcript.

Three outcomes per meeting:

- **Matched.** Run `transcript-to-actions` on it.
- **Meeting with no transcript.** Note it. Common and usually fine (someone forgot to record, or it was a call not a meeting). Count them.
- **Transcript with no meeting.** Process it anyway. Ad hoc calls are often the ones worth capturing.

Skip anything the calendar marks private, or anything matching a hard stop in `about-me.md`. Personal appointments do not get swept.

### 2. Process each matched meeting

Run the `transcript-to-actions` structure per meeting. Save to `meetings/YYYY-MM-DD-[slug]/actions.md`.

### 3. Roll up

One consolidated output, not one per meeting. The leader reads this once.

```
Swept 3 of 4 meetings from Jul 22.

DECISIONS
  Ridley pilot scoped to two DCs. (Priya, meetings/2026-07-22-ridley)
  Vendor shortlist cut to three. (Ops, meetings/2026-07-22-ops)

ACTIONS FOR YOU
  Send Priya revised timeline, due Jul 27.
  Confirm the vendor shortlist with procurement, due unknown.

NEW COMMITMENTS (appended to ledger)
  2 clear, 1 to verify.

TO VERIFY
  You may have agreed to review the vendor list by Friday. The transcript is
  ambiguous. Check meetings/2026-07-22-ops/transcript.md line 340.

NOT CAPTURED
  14:00 Board sync, no transcript found.
```

### 4. Hand off

The roll-up is available to the morning brief. Anything urgent (a commitment due today, anything matching the always-flag list) gets surfaced there. Everything else waits for the weekly review.

---

## Rules

- Same invention rules as `transcript-to-actions`. Nothing that was not said.
- Do not process the same meeting twice. Check whether `actions.md` already exists for that slug.
- Do not sweep more than 7 days back on a manual run without saying how far you went.
- If the sweep finds nothing at all and Transcripts is `connected`, say "No recorded meetings yesterday" in one line. That is not a failure and it does not need a paragraph.

## Approval rules

- May append clear commitments to `commitments.md`.
- May create meeting folders and stub person files.
- May not save person-file content without approval.
- May not send follow-ups.
- May not write a nudge about the missing transcript capability. That belongs to `connection-check`.
