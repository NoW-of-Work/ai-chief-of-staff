# connections.md — Capability Registry

> **Machine-maintained. Do not hand-fill this file.**
>
> The `onboarding` behaviour writes the first version. The `connection-check` behaviour maintains it. The `morning-brief` behaviour reads it and writes back nudge dates. A human can correct a row, but nobody needs to sit down and fill this in.
>
> This file is the system's memory of what it can actually reach. Without it, the AI Chief of Staff cannot tell the difference between "no meetings had transcripts yesterday" and "there is no transcription tool connected."

---

## 1. Why capabilities, not vendors

Every row is a **job to be done**, not a product. "Transcripts" is the capability. Otter, Fathom, Fireflies, Granola, Grain, Zoom, Teams, and Meet are providers that can fill it. Not every provider records every platform, so the right one depends on where the leader actually meets.

This keeps the rest of the system portable. Swap the provider, change one cell, and no behaviour needs editing. A behaviour asks "do I have Transcripts?" It never asks "do I have Otter?"

---

## 2. Status values

- **connected** — verified reachable on the date in Last verified.
- **missing** — no provider fills this capability.
- **failing** — a provider is configured but the last read attempt errored or returned nothing when it should have returned something.
- **unknown** — not yet probed. Only valid before the first `onboarding` run.

`failing` is treated as more urgent than `missing`. A missing tool is a gap the leader knows about. A failing tool is a gap the leader does not know about, because they still think it is running.

---

## 3. The registry

| Capability | Status | Provider | Last verified | Nudge cadence | Last nudged | Snoozed until | Dismissed |
|-----------|--------|----------|--------------|--------------|------------|--------------|-----------|
| Calendar | unknown | | | 14d | | | no |
| Email | unknown | | | 14d | | | no |
| Documents | unknown | | | 21d | | | no |
| Transcripts | unknown | | | 14d | | | no |
| Chat | unknown | | | 30d | | | no |
| Tasks | unknown | | | 30d | | | no |
| CRM | unknown | | | 45d | | | no |

Dates are `YYYY-MM-DD`. Cadence is in days. Empty means never.

Add a row only when a genuinely new capability class appears. Do not add a row per vendor.

---

## 4. What each capability unlocks

The nudge is only worth making if the leader gets something concrete. This column is what the AI Chief of Staff offers when it raises a gap.

| Capability | What the system can do once it is connected |
|-----------|--------------------------------------------|
| Calendar | Morning brief, meeting prep, working-rhythm inference, protecting deep work |
| Email | Open-loop detection, follow-up drafts, commitment capture from threads |
| Documents | Grounding briefs in real project material instead of memory |
| Transcripts | Daily sweep, decisions and action items pulled automatically, person-file updates |
| Chat | Catching commitments made in channels, not just in meetings and mail |
| Tasks | Reconciling the commitment ledger against where work is actually tracked |
| CRM | Client context in meeting prep, pipeline items in the weekly review |

---

## 5. Activation queue

When `connection-check` finds a **newly connected** capability, it appends an offer here. The next morning brief renders it as one line. It stays `pending` until the leader answers, then becomes `accepted` or `declined`. If it goes unanswered across three briefs, drop it quietly. A repeating offer is a nag with extra steps.

An offer is an offer. The AI Chief of Staff never switches on a behaviour because a tool appeared.

```
[offer] YYYY-MM-DD | [Capability] | [Provider] | [Behaviour to turn on] | status: pending / accepted / declined
```

**Pending offers:**

```
(none)
```

---

## 6. Nudge policy

A nudge about a missing capability surfaces only when **all three** gates pass.

1. **Cadence.** At least `Nudge cadence` days since `Last nudged`.
2. **Not silenced.** `Snoozed until` is empty or in the past, and `Dismissed` is `no`.
3. **Relevant trigger.** Something happened that day where the missing capability would have helped. Being due is not a reason to speak.

Trigger conditions, per capability:

| Capability | Nudge only when |
|-----------|----------------|
| Calendar | The leader asks for a brief or prep and there is no schedule to read |
| Email | There were external meetings and no inbox to check for follow-through |
| Documents | A brief had to label something `(not connected)` for a project the leader named as a priority |
| Transcripts | The leader had two or more meetings yesterday and nothing captured them |
| Chat | A commitment surfaced that clearly originated in a channel the system cannot read |
| Tasks | The commitment ledger has gone stale for more than 14 days |
| CRM | Meeting prep for an external party returned no history at all |

**Hard cap: at most one capability nudge per morning brief.** If several are eligible and triggered, surface the highest-value one and hold the rest. Value order, high to low: Calendar, Email, Transcripts, Documents, Tasks, CRM, Chat.

If a nudge and an activation offer are both queued for the same brief, the **offer wins**. It is news, and it is the one the leader can act on today. The nudge waits for its next cadence window and its `Last nudged` date does not move.

---

## 7. Silencing

The leader controls this file by saying so in plain language. The AI Chief of Staff writes the result here.

| The leader says | What gets written |
|----------------|------------------|
| "Not now" / "later" | `Snoozed until` = today + cadence |
| "Not now" a second time | `Dismissed` = yes. Two soft noes are a hard no. |
| "Never" / "stop asking" | `Dismissed` = yes |
| "Ask me again in a month" | `Snoozed until` = today + 30 days |

A dismissed capability is never nudged again. It still gets picked up as **newly connected** if the leader connects it later, because that is news rather than nagging.

---

## 8. Change log

`connection-check` appends one line per run. Keep the last 20. Archive the rest.

```
YYYY-MM-DD | [Capability] | [old status] -> [new status] | [provider] | [action taken]
```

**Entries:**

```
(none yet — run the onboarding behaviour to populate this file)
```
