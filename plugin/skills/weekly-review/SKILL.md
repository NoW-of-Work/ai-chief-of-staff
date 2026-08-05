---
name: weekly-review
description: "Monday look back and forward: what moved, what slipped, where the time went, drift against what you said you are not doing, next week's focus, and workspace maintenance. 500 words."
---

# weekly-review

## Trigger

- Monday morning, on a schedule, before or alongside the morning brief.
- On demand: "weekly review", "how did last week go", "what am I behind on".

## Reading order

1. `CLAUDE.md`.
2. `connections.md`. Run `connection-check` first if it has not run this week.
3. `my-work.md`, all of it. This is the one behaviour that reads the whole file.
4. `about-me.md`, sections 4, 6, 7.
5. `commitments.md`, all of it.
6. Last week's `briefs/`, both morning briefs and closes.
7. Last week's calendar as it actually ran. Next week's calendar.
8. `meetings/` from last week.

---

## Structure

500 words. Longer than the daily outputs because it is read once and it is where decisions get made.

### 1. What moved

Against the priorities in `my-work.md` section 2. One line per priority, with what actually happened.

Be specific about the ones that did not move. "Priority 3 did not move in five working days" is the sentence that makes the leader decide something. "Progress was limited on priority 3" is not.

### 2. What slipped

Commitments that went stale, using the thresholds in `commitments.md` rule 4:

- `Active` for more than 14 days.
- `Awaiting` for more than 7 days.

For each, say how long, to whom, and propose an action: chase it, release it, or renegotiate the date. Do not just list them. A list of stale items with no proposal becomes wallpaper by week three.

### 3. Where the time went

Compare last week's calendar against the target distribution in `my-work.md` section 6.

Report the drift, not the whole breakdown. "You targeted 40% client time and spent 18%. Internal meetings took the difference" is the useful version.

Flag anything that ate a protected block from `about-me.md` section 7. If the same block got eaten three weeks running, it is not a block any more and the leader should either defend it or drop it. Say that.

### 4. Drift check

Anything from `my-work.md` section 5 (what we are not doing) that showed up in last week's calendar, mail, or meetings.

This is the section leaders find most useful and it is the one most often skipped. Name it directly. "You spent 3 hours on the website redesign, which section 5 says is not this quarter."

### 5. Next week

Two or three things. What the week should be for. Grounded in the priorities, the slipped commitments, and what is already fixed on next week's calendar.

Name the tradeoff. If taking on the slipped item means priority 4 does not move again, say so.

### 6. Workspace maintenance

The weekly review is where the system keeps itself honest. Check and propose:

- **Stale inferences.** Anything still marked `(inferred)` in `about-me.md` or `my-work.md` after four weeks. Ask, or drop it.
- **Finished priorities.** Anything in section 2 that looks done. Propose cutting it.
- **Missing priorities.** Anything eating real calendar time that is not on the list. Propose adding it, or flag it as drift.
- **Repeated corrections.** If the leader corrected the same thing three times this month, propose the edit to `about-me.md` that stops it happening again.
- **Onboarding gaps.** Anything the leader skipped during onboarding. Ask for one of them, not all of them. One per week gets answered. Six do not.

Cap this section at three proposals. It is maintenance, not an audit.

---

## Rules

- Do not restate the daily briefs. This is the pattern across the week, not a digest of it.
- Do not soften a slip. The leader can handle "this did not move" and cannot use "this had limited progress".
- Do not propose more than three changes to the workspace in one review.
- Do not raise capability gaps. `connection-check` decides and the morning brief delivers. This holds even here.
- If last week was genuinely quiet, the review is short. A short review of a quiet week is correct output.

## Approval rules

- May save to `briefs/YYYY-MM-DD-weekly.md`.
- May append and update `commitments.md` with sourced entries.
- May archive commitments older than 90 days to `archive/commitments-[YYYY]-Q[N].md`.
- May **not** change priorities in `my-work.md` without approval, per `CLAUDE.md` gate 7. Propose, then wait.
- May not release a commitment on the leader's behalf. Propose it.
- May not send anything.
