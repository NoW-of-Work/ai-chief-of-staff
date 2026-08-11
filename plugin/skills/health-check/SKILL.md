---
name: health-check
description: "Audit whether the workspace is actually configured: blocking gaps, stale files, contradictions between files, output folders that are not filling, and one honest verdict. 350 words. Monthly."
---

# health-check

## Trigger

- Scheduled: monthly, on the first Monday, after `connection-check` and before `weekly-review`.
- After any run of `onboarding`, including a re-run, so the leader sees what setup left behind.
- On demand: "is this thing actually working", "check the setup", "why are the briefs so thin".

## The rule

**350 words, hard cap.** A check that always says everything is fine buys a quarter of false confidence, and twenty-two findings in file order is a document nobody opens. Six findings in fix order gets read before the first meeting. When you run over, cut in this order:

1. Contradictions between files. Slot 4 is the finding that can wait a month.
2. Then staleness the weekly review already flagged. It keeps until next month.
3. **Never the verdict.** It is the only line the leader is guaranteed to read.

## Reading order

1. `CLAUDE.md`. Read it for the gates, and read section 1 for bracketed fields.
2. `connections.md`, the registry rows and the change log. The log only moves when a status changes, so an empty log proves nothing on its own. Read the Last verified dates on the rows that still read `connected`. A `failing` row keeps its old date on purpose, so that date measures how long the tool has been down and says nothing about the check.
3. `about-me.md`, all of it, sections 6 and 8 closest (always flag, hard stops).
4. `my-work.md`, all of it, sections 1 and 5 closest (current strategic priority, what we are not doing).
5. `commitments.md`, all of it, including Released and Closed.
6. `tomorrow.md`, for its date line only.
7. `briefs/`, file names and dates for all of them, plus the contents of three things: last month's four `-weekly.md` files, the previous `-health-check.md`, and the newest `-brief.md`. That is the only reading in this folder. `meetings/` and `people/`, file names and dates only.
8. Today's calendar, only far enough to confirm the leader has meetings this system should have been prepping.

If `connections.md` is missing, or every row still reads `unknown`, stop the audit and report one finding: onboarding has not run. Everything else is downstream of that. On a first run, when `briefs/` holds nothing and no close has run, checks 3, 4 and 5 have nothing to measure: `commitments.md` is still the blank template and `people/` holds only its stub. Run checks 1 and 2, and let the verdict say the output checks start next month. A re-run over a populated workspace runs all five.

---

## Job A: Find what is actually wrong

Five checks. Run all five before ranking anything, even when the first one already looks bad.

### 1. The four fields

Count nothing. The templates are built to survive half-empty, and a bracketed field is a note rather than a finding. Four are not:

| Field | What goes dead without it |
|-------|--------------------------|
| `about-me.md` section 6, always flag | Nothing is ever unmissable |
| `about-me.md` section 8, hard stops | The only limits are the manual's |
| `my-work.md` section 1, strategic priority | Every brief invents its own top line |
| `my-work.md` section 5, what we are not doing | Drift never gets called drift |

Check `CLAUDE.md` as well. `[LEADER NAME]`, `[TITLE]`, or `[ORGANIZATION]` still sitting in section 1 means the mandate was never written for anyone in particular.

### 2. What the registry is claiming

Two failure shapes in `connections.md`, and they look nothing alike. A row still reading `unknown` after `onboarding` has run means the probe never happened or never got saved. Until that is fixed, every absence downstream of it is unexplained rather than informative.

A row reading `connected` with a Last verified date more than 14 days old is an assertion nobody has tested. `connection-check` refreshes every row weekly, so an old date is a fact about the check and says nothing about the tool. If several rows are stale by the same amount, that is one finding: `connection-check` last ran on [date], [N] days ago. Give the date and the day count. Do not probe it here.

### 3. Staleness

- `tomorrow.md` written for a date that has passed. One day past is normal. Two weeks past means the leader stopped using the close, and `end-of-day-close` has been drafting into a file nobody opens.
- A priority in `my-work.md` section 2 quoted unchanged in all four of last month's weekly reviews with nothing recorded against it in `commitments.md`. A priority that survives a month of reviews without moving is finished or abandoned, and the brief has been quoting it either way.
- Items in `commitments.md` past the rule 4 threshold for their status, `Active` beyond 14 days or `Awaiting` beyond 7, that were also flagged in a weekly review and never moved. Something raised three times and never resolved is a decision the leader has already made quietly.

### 4. Files that disagree

- Every priority in `my-work.md` section 2 against `commitments.md`, skipping any priority check 3 already flagged. A priority with nothing supporting it is either not being worked on, or is being worked on where the ledger cannot see. One line either way.
- Every name in the always-flag list against `people/`. Someone the leader can never miss, with no file, means every prep involving them starts cold.
- Every name attached to a commitment against the rest of the workspace. A person who owes the leader something and appears in no meeting file, no person file, and no key-relationships row is usually a name the system captured wrong. Label it `(needs check)` and name what to confirm and where. Do not change the name.

### 5. Whether anything is actually landing

List `briefs/`, `meetings/`, and `people/`. For `meetings/` and `people/`, file names and dates are enough. Do not open them. Judge whether the brief is running from the `-brief.md` names alone. Closes, triage passes and this audit live in the same folder and none of them is evidence the brief ran.

An empty `briefs/` after a week of working days means the scheduled task is not running, or it is running and writing somewhere else. The leader tells the two apart in under a minute by opening the task and reading the folder name. An empty `meetings/` while the calendar shows external meetings means `meeting-prep` has never been used. That is a habit finding. Say it once and do not raise it again next month.

---

## Job B: Rank it, then say one true thing

Six slots, below. The table is not the slots. It is the severity order you rank findings in before you place them, and one row of it is a band. A slot with nothing in it does not render.

| What is broken | What it costs |
|---------------|--------------|
| Nothing is running | Every other finding is theoretical |
| The registry is lying | Silence and blindness read the same |
| The four fields are empty | Every output is generic and nobody knows why |
| The inputs are stale | The brief is working from a quarter that ended |
| The files disagree | One brief in five carries a wrong fact |

Slots 1 and 6 draw from every band. Inside a band, the shorter fix goes first, so a leader with four spare minutes can work top down and stop when the time runs out.

### 1. Fix first

Exactly one finding. The highest-ranked one, with the action written as something the leader can do in under a minute. Whatever you lift into this slot does not render again in its band. One, because a first thing with four parts is not a first thing. If the top finding needs longer than a minute, say how long. An honest twenty-minute price tag gets scheduled. A fake one-minute price tag gets started and abandoned.

### 2. Blocking

Findings that stop a behaviour producing correct output. Anything checks 1 and 5 turned up, and the `unknown` rows from check 2. If nothing is blocking, **this slot does not render.** Each one gets three parts: what is empty, what the last month of output lost because of it, and the fix. Name a real brief where it showed, from the newest `-brief.md` or from last month's reviews. Without a cost attached, this slot is a template scold.

### 3. Degrading

Findings that thin the output without stopping it. The untested claims from check 2, and everything check 3 called stale. Give the day count and the fix, every time. "Stale" is an opinion. "Awaiting since Jul 2, 32 days" is a fact the leader can act on this morning.

### 4. Worth knowing

Contradictions between files, capped at three. More than three and the leader reads none of them. A contradiction is not proof of an error. Say which file you believe and say why. `commitments.md` outranks a transcript, and a meeting file outranks a person file, per `CLAUDE.md` section 5.

### 5. What could not be checked

Only what the audit genuinely could not reach. `(not connected)` when `connections.md` has the capability as `missing` or `failing`. `(no source)` when the capability works and the file is simply empty. The first is the system's problem. The second is the leader's. If everything was reachable, this slot does not render.

### 6. The verdict

One sentence. Is this system doing its job right now, yes or no. This slot always renders and it is the only one that does. A run that found nothing renders slot 6 alone, and that is the correct shape for a workspace in good order.

The sentence opens with `Yes` or with `No`, then one clause of evidence. Never write "mostly", "broadly", "largely", or "on track".

> Yes. The brief has run every working day for three weeks and the four fields are filled.

---

## What this behaviour must never do

- **Never report a pass you did not check.** A capability you could not reach belongs in slot 5, and it never counts toward a `Yes`.
- **Never render a finding without a fix.** A finding with no next step is wallpaper by the second run.
- **Never count placeholders.** A tally of bracketed fields tells the leader nothing.
- Do not re-raise a finding the leader declined last run. It is in the `DECLINED` block of the previous audit. Move past it.
- Do not raise capability gaps as nudges. `connection-check` decides and the morning brief delivers. That holds here too.
- Do not re-propose what `weekly-review` section 6 proposed in the four reviews you just read. That section handles stale inferences, finished priorities, and onboarding gaps weekly. This audit only reports them when all four went past and nothing moved.

## Approval rules

- Saves the audit to `briefs/YYYY-MM-DD-health-check.md`, every run, and that is the only file it writes on a run nobody is watching. Below the verdict, outside the 350 words, the file carries a `DECLINED` block: one line per finding the leader declined this run, with the date. That block is written for next month's run and never renders in the output.
- May create a stub `people/[name].md` for a name that carries a commitment and has no file, holding the name and the commitment reference only.
- May propose an exact edit to `about-me.md`, `my-work.md`, or `CLAUDE.md`, and write it if the leader says yes in the same session.
- May **not** write that edit on a scheduled run, or on any run where the leader is not there to answer. Filling a bracketed field is a decision nobody has made yet. Priorities are `CLAUDE.md` gate 7.
- May **not** write to `connections.md`. Statuses, providers, and Last verified dates belong to `connection-check`, which probes.
- May not close, release, or re-date a commitment this audit judged stale. Propose it.
- May not send anything, and may not report this audit to anyone but the leader.

## Worked example

```
FIX FIRST
  briefs/ holds three files, none newer than Jul 14. 14 working days, no brief.
  Fix: open the scheduled task and read the folder name it points at.

BLOCKING
  my-work.md section 1, strategic priority, still bracketed. Every brief this
  month opened off a document title. See briefs/2026-07-28-brief.md, line 1.
  Fix: one sentence, section 1.

DEGRADING
  connections.md: Email reads connected, Last verified 2026-06-02, 62 days.
  Fix: say "check my connections" and let connection-check probe the row.
  commitments.md: two Awaiting items owed to you since Jul 2, 32 days, raised in
  three reviews, neither moved. (source: briefs/2026-07-27-weekly.md)
  Fix: chase both, or release them. chase carries the drafts.

WORTH KNOWING
  Dev Ramanathan (Teale, ops lead) carries two commitments in commitments.md and
  appears in no other file. Confirm the name before the next prep. (needs check)
  Priority 2, warehouse pilot, has nothing behind it in commitments.md. Add
  the commitment, or cut the priority.

VERDICT
No. It is briefing off a profile nobody finished, and it stopped briefing at
all 14 working days ago.
```

The verdict is a no and it names the two facts that make it a no. Every finding carries a day count or a file name, and a fix.
