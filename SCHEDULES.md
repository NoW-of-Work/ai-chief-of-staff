# SCHEDULES

**AI Chief of Staff, v1.1.0. Created by The NoW of Work.**

Every recurring job in the system, as text you can copy and paste. Nine of the thirteen behaviours can run on a schedule, and they take ten scheduled tasks, because inbox triage runs twice a day. The other four need a subject only a person can give, so they run when asked.

**On ChatGPT the finished clock is a plan requirement before it is a schedule.** Ten active tasks needs Pro, Business, Edu, or Enterprise. Plus caps at five and Go at three, so those two plans run a shorter clock, and **Add them in this order** says which five to keep. A free account cannot schedule anything at all. Claude has no equivalent cap.

---

## Read this once, then every block below obeys it

**A scheduled run starts with no memory of any conversation.** It has never met the leader. It does not know which folder you mean, which files exist, or what you agreed in the session last Tuesday. It gets the prompt text and nothing else.

So every prompt below names the workspace folder in its first line. A prompt that only says "run the morning brief" produces a generic summary of the day with none of the leader's context in it. It does that silently, every morning, for weeks.

Five consequences worth stating plainly.

**Every block below says `[WHERE THE WORKSPACE LIVES]`. Replace it before you paste.** Write the real home of the folder, in the words the leader's own setup uses: files saved to the Claude account, a folder connected in Cowork, a connected app such as Google Drive. `READ-ME-FIRST.md` Path A step 2 decided it for Claude, Path C step 5 for ChatGPT. A prompt that names the wrong home fails silently every morning, and it reads exactly like a prompt that names the right one.

**The folder has to sit somewhere a scheduled run can reach.** A scheduled task cannot reach a folder that only exists on a laptop, and the brief has to arrive before the leader opens one.

**The manual has to be named too.** In Claude that is `CLAUDE.md`. In ChatGPT it is `PROJECT-INSTRUCTIONS.md`. The copy pasted into the project's custom instructions serves the chats the leader opens. A scheduled run needs the copy that sits in the connected folder, which is why every block below names the file rather than assuming it. Every behaviour assumes the manual has been read first, and a scheduled run has not read anything yet.

**A ChatGPT scheduled run cannot write a file back into the workspace.** In a session the leader opens, ChatGPT writes through a connected app and asks for approval before each write. A scheduled run has nobody in the room to give that approval, so every block below prints instead, and the leader pastes it in. Paste it into the connected folder, because that is the copy tomorrow's scheduled run reads. The project upload is a second copy and it only serves the chats the leader opens themselves. Two copies that drift apart is real friction, and it belongs in the handover rather than in a surprise at week three. Most of those pastes are optional. The one that genuinely matters is `connections.md`, because the nudge dates are what stop the same missing tool being mentioned every second week.

**A ChatGPT scheduled task cannot read the project's files, and creating the task inside the project does not change that.** OpenAI's help article on scheduled tasks says it plainly: a task created in a project that has files will not be able to access those files. Project files are for chats the leader opens themselves. So every ChatGPT block below names a connected app in its first line, exactly as the Claude blocks do, and the workspace has to live in that app before any of this runs unattended. `READ-ME-FIRST.md` Path C step 5 is where that home was decided. Whatever the run still cannot look up has to sit in the prompt text itself, because the prompt is the only thing that reaches it.

---

## Add them in this order

Not all at once. **Week one is the morning brief and nothing else.**

A leader who ignores four of five outputs stops trusting the fifth, and by then you cannot tell which one failed.

**On ChatGPT, count the tasks against the plan before week one.** The finished clock is ten scheduled tasks, and ChatGPT caps how many can be active at once: 3 on Go, 5 on Plus, 10 on Business and Edu, 15 on Pro and Enterprise. Go runs out during week two. Plus runs out during week three, halfway through the ramp, and the leader finds out when a task refuses to save. Say the number at handover rather than in week four.

A leader staying on Plus keeps the daily loop and drops the rest: `morning-brief`, `connection-check`, both `inbox-triage` passes, and `end-of-day-close`. If the weekly review matters more to them than a second mail pass, trade the afternoon triage for it. The five that come off the schedule still work when asked, and asked is the better mode for them anyway, because a chat the leader opens inside the project can read the project's files and a scheduled run cannot. Claude has no equivalent cap.

| Week | Add | Why here |
|------|-----|----------|
| 1 | `morning-brief` | It is the one the leader reads. Everything else exists to make it better. Wait until it has been read five days running |
| 2 | `connection-check` | Silent most weeks, so it costs the leader nothing. It also makes every later job honest, because the registry separates "nothing happened" from "I cannot see what happened" |
| 3 | `daily-transcript-sweep` | It feeds the brief, so add it once the brief is trusted. It exits silently until a transcription tool is connected, which makes it a safe third |
| 3 | `inbox-triage` | The other input job, and the first one that hands the leader something to approve. Say out loud that the drafts sit until the leader sends them, before the first one appears |
| 4 | `end-of-day-close` | It asks the leader for a decision every evening, and an evening decision is harder to keep than a morning one. Approving `tomorrow.md` takes thirty seconds and it changes tomorrow's brief |
| 5 | `weekly-review` | It reviews history. There is nothing useful to look back on until four weeks of briefs, closes, and commitments exist |
| 5 | `chase` | It runs off what the review names as slipped, so it has nothing to work with until the review is live |
| Month 2 | `health-check` | It audits the setup, so it needs a month of setup to audit. Run it before the 30-day check-in and read the verdict before you open a file |
| Month 3 | `decision-brief`, review pass | It reads `decisions.md`, and that file is empty until the leader has closed a call and logged it. Add it once two or three entries are sitting there with review dates on them |

Two weeks carry a pair. Week 3 adds both input jobs, which each read `connections.md` first and produce nothing when their source is missing. Week 5 adds the review and the chase that runs off it.

Otherwise the order is roughly least demanding to most demanding. The brief asks nothing of the leader. The close asks for a decision every evening. Put four weeks between those two.

---

## 1. Morning brief

**What it does.** Today's priorities, the meetings that need something, open loops, drafts waiting on a yes, and at most one line about a capability gap. Under 400 words.

**When.** Weekdays, 30 to 45 minutes before the leader's first meeting, or before they open a laptop. Whichever is earlier. If the transcript sweep is running, the brief goes after it. In Claude that means its output lands in the brief. On ChatGPT see the clock section.

**Claude**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
CLAUDE.md first.

Run the morning-brief behaviour for today.

Label anything you guessed. Use (inferred), (uncertain), (no source), or
(not connected). An unlabelled claim has to be traceable to a file or a
source.

Save the output to ai-chief-of-staff/briefs/ named with today's date,
for example 2026-07-14-brief.md.

If you write a capability nudge or an activation offer, update the
matching dates in connections.md.
```

**ChatGPT**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
PROJECT-INSTRUCTIONS.md in that folder first. You are running on a
schedule, so the project's own files are out of reach.

Run the morning-brief behaviour for today.

Label anything you guessed. Use (inferred), (uncertain), (no source), or
(not connected). An unlabelled claim has to be traceable to a file or a
source.

Print the brief in the chat. Do not claim to have saved it.

If a capability nudge or an activation offer belongs in this brief, print
the one line of connections.md that needs updating, so I can paste it back.
```

**What is different in ChatGPT.** The brief lives in the chat and the leader keeps it or does not, which is fine for something read once. Paste the changed `connections.md` line back into the connected folder weekly and leave the rest. A line pasted only into the project copy is a line tomorrow's run will not see.

---

## 2. Connection check

**What it does.** Compares the live connectors against `connections.md`. Updates the registry, queues an activation offer for anything newly connected, and flags anything that has quietly stopped working. Decides, rarely, whether a missing tool is worth one line in tomorrow's brief.

**When.** Weekly, Monday, one hour before the morning brief, so whatever it finds lands in that day's brief.

**Claude**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
CLAUDE.md first.

Run the connection-check behaviour.

Update connections.md in that folder: statuses, providers, last verified
dates, the activation queue, and the change log.

Report only what changed. If nothing changed, say nothing.
```

**ChatGPT**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
PROJECT-INSTRUCTIONS.md in that folder first. You are running on a
schedule, so the project's own files are out of reach.

Run the connection-check behaviour.

You cannot list your own connectors, so probe by use. Try one small read
against every capability connections.md says is connected.

Print the full updated connections.md in one code block so I can replace
the file in that folder. Print a one-line summary of what changed above it.

If nothing changed, say so and print nothing else.
```

**What is different in ChatGPT.** It cannot enumerate its own connectors, so it tests each one by trying to read from it, which is slower and slightly less certain. It prints the whole registry for the leader to replace in the connected folder, and a month of skipping that paste stops the nudge dates moving. Replace the project copy too when you get to it, so an on-demand chat and a scheduled run do not disagree about what is connected.

---

## 3. Daily transcript sweep

**What it does.** Takes yesterday's recorded meetings, turns each one into decisions and action items, and appends new promises to the ledger. Nobody has to ask.

**When.** Daily, 30 minutes before the morning brief, so its output can feed into the brief. On ChatGPT see the clock section.

**Claude**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
CLAUDE.md first.

Check the Transcripts row in connections.md before anything else. If it is
not connected, stop and produce no output at all.

Otherwise run the daily-transcript-sweep behaviour for yesterday.

Save each meeting to ai-chief-of-staff/meetings/ in a dated folder,
for example 2026-07-14-ridley-review/actions.md.

Append new commitments to commitments.md. Do not draft or send anything.
```

**ChatGPT**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
PROJECT-INSTRUCTIONS.md in that folder first. You are running on a
schedule, so the project's own files are out of reach.

Check the Transcripts row in connections.md before anything else. If it is
not connected, stop and produce no output at all.

Otherwise run the daily-transcript-sweep behaviour for yesterday.

Print one code block per meeting, headed with the filename it should be
saved as. Then print any new commitments as lines to append to
commitments.md.

Do not draft or send anything.
```

**What is different in ChatGPT.** The meeting folders do not create themselves, so the leader saves each block into the connected folder by hand, which is real friction on a day with four recorded calls. Run it weekly instead, or paste only the commitment lines, since the ledger is the part the other behaviours read.

**Silence is the correct output here.** Until a transcription tool is connected, this job produces nothing, every day. That is designed. Tell the leader before you schedule it, or the first week of nothing reads as a broken job.

---

## 4. Inbox triage

**What it does.** Mail since the last pass, cut to what needs a person. Decisions waiting on the leader, drafted replies, promises made in both directions, and a count of what it left alone. Under 350 words.

**When.** Twice on a working day. Once about fifteen minutes before the morning brief, so the brief knows what arrived overnight, which on ChatGPT works differently and the clock section says how. Once an hour before the hard stop in `about-me.md` section 2, so the afternoon does not carry into tomorrow.

This is the one job that runs twice, so it takes two scheduled tasks and two prompts. Paste the same text into both and the second run reaches for the first run's filename.

**Claude, morning pass**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
CLAUDE.md first.

Check the Email row in connections.md before anything else. If it is not
connected, stop and produce no output at all.

Otherwise run the inbox-triage behaviour. Triage mail received since the
last pass. Draft replies. Do not send any of them.

Save the pass to ai-chief-of-staff/briefs/ named with today's date and the
suffix -triage-am, for example 2026-07-14-triage-am.md.

Append any new commitments to commitments.md.
```

**Claude, afternoon pass**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
CLAUDE.md first.

Check the Email row in connections.md before anything else. If it is not
connected, stop and produce no output at all.

Otherwise run the inbox-triage behaviour. Triage mail received since the
last pass. Draft replies. Do not send any of them.

Read this morning's brief and this morning's triage pass in
ai-chief-of-staff/briefs/ first. Do not repeat any decision the morning
pass already surfaced.

Save the pass to ai-chief-of-staff/briefs/ named with today's date and the
suffix -triage-pm, for example 2026-07-14-triage-pm.md.

Append any new commitments to commitments.md.
```

**ChatGPT, morning pass**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
PROJECT-INSTRUCTIONS.md in that folder first. You are running on a
schedule, so the project's own files are out of reach.

Check the Email row in connections.md before anything else. If it is not
connected, stop and produce no output at all.

Otherwise run the inbox-triage behaviour. This is the morning pass. There
is no earlier pass you can read, so triage the last 24 hours and say so in
one clause. Draft replies. Do not send any of them.

Print the pass in the chat, headed Morning pass. Then print any new
commitments as lines to append to commitments.md.

Do not tell me anything has been sent.
```

**ChatGPT, afternoon pass**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
PROJECT-INSTRUCTIONS.md in that folder first. You are running on a
schedule, so the project's own files are out of reach.

Check the Email row in connections.md before anything else. If it is not
connected, stop and produce no output at all.

Otherwise run the inbox-triage behaviour. This is the afternoon pass.
Triage mail received since 06:00 today. You cannot read this morning's
pass, so where a decision may already have been raised, list it anyway and
mark it (possibly raised this morning). Draft replies. Do not send any of
them.

Print the pass in the chat, headed Afternoon pass. Then print any new
commitments as lines to append to commitments.md.

Do not tell me anything has been sent.
```

**What is different in ChatGPT.** Neither pass leaves a file, so the afternoon run cannot see the morning one and the two blocks above are not interchangeable. The afternoon block starts its window at 06:00 rather than at midday on purpose. A window that starts after the morning pass leaves the hours between them triaged by nobody, so the two overlap and the overlap is marked. The cost is a decision listed twice on a busy day, marked rather than hidden. If that irritates the leader more than a missed decision would, drop the afternoon task and keep one pass.

**The drafted replies are the thing to watch.** This is the only scheduled job that writes text addressed to another person twice a day. A leader who gets used to skimming them will eventually approve one they have not read. Say at handover that the system has no way to send, and that every draft waits in the file until they copy it out themselves.

---

## 5. End-of-day close

**What it does.** What moved against this morning's priorities, what came in, what changed in the ledger, and a drafted `tomorrow.md` for approval. Under 200 words, plus the draft.

**When.** Daily, about 30 minutes before the hard stop recorded in `about-me.md` section 2. Early enough that the leader is still at a desk. Late enough that the day has happened.

**Claude**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
CLAUDE.md first.

Run the end-of-day-close behaviour for today.

Save the close to ai-chief-of-staff/briefs/ named with today's date,
for example 2026-07-14-close.md.

Draft tomorrow.md and show it to me in full. Do not save tomorrow.md
until I say yes.
```

**ChatGPT**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
PROJECT-INSTRUCTIONS.md in that folder first. You are running on a
schedule, so the project's own files are out of reach.

Run the end-of-day-close behaviour for today.

Print the close. Then print the drafted tomorrow.md as a separate code
block, so I can replace the file in that folder if I approve it.

Do not tell me it has been saved.
```

**What is different in ChatGPT.** Nothing about the approval gate. `tomorrow.md` is never written without a yes, and the leader copies the approved block over the file in the connected folder. Tomorrow's brief reads that copy, so that is the one that has to change. Same decision, one more step.

**One warning worth giving in the session.** If the leader stops approving `tomorrow.md`, every morning brief afterwards starts from a stale premise. Better to turn this job off than to let it draft into a void.

---

## 6. Weekly review

**What it does.** What moved, what slipped, where the time actually went, drift against what the leader said they are not doing, next week's focus, and workspace maintenance. Around 500 words.

**When.** Weekly, Monday morning, right after the morning brief, which is what the behaviour's own trigger says. It reads the week that just ended, so anything earlier than Monday reviews a week that is not finished.

**Claude**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
CLAUDE.md first.

If connection-check has not run this week, run it first.

Run the weekly-review behaviour for the week that just ended.

Label anything you guessed. Use (inferred), (uncertain), (no source), or
(not connected). An unlabelled claim has to be traceable to a file or a
source.

Save the output to ai-chief-of-staff/briefs/ named with today's date,
for example 2026-07-13-weekly.md.

Propose ledger closes and archive moves. Do not make them without a yes.
```

**ChatGPT**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
PROJECT-INSTRUCTIONS.md in that folder first. You are running on a
schedule, so the project's own files are out of reach.

If connection-check has not run this week, run it first.

Run the weekly-review behaviour for the week that just ended.

Label anything you guessed. Use (inferred), (uncertain), (no source), or
(not connected). An unlabelled claim has to be traceable to a file or a
source.

Print the review. Then list the ledger closes and archive moves you propose,
numbered, so I can answer with the numbers I approve.

Do not print an edited commitments.md until I have answered.
```

**What is different in ChatGPT.** The review reads across four weeks of history, and on a schedule it reads that history out of the connected folder rather than the project. Once the folder holds a few dozen files ChatGPT retrieves rather than reads everything, so quality falls as the workspace grows. Archive anything older than a quarter, and name the window in the prompt when it drifts, for example "the week of July 6 to July 10."

---

## 7. Chase

**What it does.** What the leader is owed and has not been given. A shortlist of stale items, a release call on the ones that died, drafts sized to the relationship, and escalation notes for anything blocking a priority. Under 350 words.

**When.** Weekly, Thursday morning. Monday's review names what slipped, and three days is long enough for the person to answer without being asked. The behaviour's own trigger says the same thing, and it reads Monday's review first so a release it already proposed does not get proposed twice.

**Claude**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
CLAUDE.md first.

Run the chase behaviour against commitments.md, filtered to what I am
still owed.

Draft the chases and show them to me. Do not send anything.

Save the drafts to ai-chief-of-staff/briefs/ named with today's date,
for example 2026-07-16-chases.md.
```

**ChatGPT**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
PROJECT-INSTRUCTIONS.md in that folder first. You are running on a
schedule, so the project's own files are out of reach.

Run the chase behaviour against commitments.md, filtered to what I am
still owed.

Draft the chases and show them to me. Do not send anything.

Print each draft as its own code block, headed with the person's name.
```

**Three per run is a hard cap and it is load-bearing.** A run that proposes eleven nudges gets none of them sent, because the leader reads two and closes the file. Some weeks it proposes one, and some weeks nothing clears the gates. That is the cap working.

---

## 8. Health check

**What it does.** Audits whether the workspace is actually configured. Blocking gaps, stale files, contradictions between files, output folders that are not filling, and one verdict. Under 350 words.

**When.** Monthly, first Monday, after the connection check and before the weekly review. It reads the registry to decide what a stale date means, so a registry nobody refreshed makes the audit wrong.

**Claude**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
CLAUDE.md first.

Run the health-check behaviour.

Report blocking gaps, stale files, contradictions between files, and output
folders that are not filling.

Do not edit any of the files you are auditing. Every finding is a proposal.

Save the audit to ai-chief-of-staff/briefs/ named with today's date and the
suffix -health-check, for example 2026-07-06-health-check.md.

Print the verdict line first.
```

**ChatGPT**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
PROJECT-INSTRUCTIONS.md in that folder first. You are running on a
schedule, so the project's own files are out of reach.

Run the health-check behaviour.

Report blocking gaps, stale files, contradictions between files, and output
folders that are not filling.

Do not edit any of the files you are auditing. Every finding is a proposal.

Print the verdict line first. Then print the whole audit in one code block,
headed with the filename it should be saved as, for example
2026-07-06-health-check.md.
```

**This is the one audit that leaves a file behind.** It edits nothing it reads, and it writes its own output every run, to `briefs/YYYY-MM-DD-health-check.md`. Next month's audit reads that file back, which is how it tells a finding the leader already declined from one nobody has seen. In Claude it saves it. On ChatGPT it prints it and the leader saves it into the connected folder, and a month of skipping that paste means the next audit re-raises what this one already settled.

**Read the verdict line first.** It is the one line the behaviour will not cut, and it is allowed to say no. If it reports that no source file has been touched since setup, the deployment is failing quietly and scheduling more jobs makes it worse.

---

## 9. Decision review

**What it does.** Reads `decisions.md` against today's date. Surfaces entries whose review date has passed, entries where a condition under **Would change my mind** has come true, `Open` entries about to be forced, and `To verify` entries still waiting on the leader. Nothing else from the file renders.

**When.** Weekly, Monday, after the morning brief and before the weekly review. `weekly-review` renders what this pass finds, in its decisions slot, so it has to run first. `decision-brief` carries this as its own second trigger, and nothing else in the system checks a review date.

**Claude**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
CLAUDE.md first.

Run the decision-brief behaviour in review mode against decisions.md.

Surface only: entries whose Review on date has passed, entries where a
condition under Would change my mind has come true, Open entries whose
Forced by date lands in the next 14 days, and To verify entries still
waiting on me.

Do not promote any entry to Made. Do not edit the fields of an existing
Made entry.

Save to ai-chief-of-staff/briefs/ named with today's date, for example
2026-07-13-decisions.md.

If nothing has come due, say nothing.
```

**ChatGPT**

```
Read the ai-chief-of-staff folder in [WHERE THE WORKSPACE LIVES]. Read
PROJECT-INSTRUCTIONS.md in that folder first. You are running on a
schedule, so the project's own files are out of reach.

Run the decision-brief behaviour in review mode against decisions.md.

Surface only: entries whose Review on date has passed, entries where a
condition under Would change my mind has come true, Open entries whose
Forced by date lands in the next 14 days, and To verify entries still
waiting on me.

Do not promote any entry to Made. Do not edit the fields of an existing
Made entry.

Print the review. Print any proposed entry as its own code block so I can
paste it into decisions.md in that folder, after I confirm the outcome in
my own words.

If nothing has come due, say nothing.
```

**Most Mondays this produces nothing, and that is the file holding.** It speaks when a decision made in July stops matching the facts in September. Without it, `decisions.md` is an archive nobody reopens, and the **Would change my mind** field is the only reason to keep the file at all.

**It reads. It does not close.** Promoting an entry to `Made` needs the leader saying what they decided, in their own words, in that session. That is gate 11 in `CLAUDE.md`, and a scheduled run has nobody in the room.

---

## One clock, all nine

A worked week, for a leader whose first meeting is at 08:00 and whose hard stop is 16:30. Adjust the offsets, keep the order.

Nine behaviours, ten rows. `inbox-triage` appears twice and takes two tasks, so a consultant counting entries in the Scheduled panel should find ten, not nine. Anything past ten means something was installed twice.

| Time | Job | Days |
|------|-----|------|
| 06:00 | `connection-check` | Monday |
| 06:15 | `health-check` | First Monday of the month |
| 06:30 | `daily-transcript-sweep` | Weekdays |
| 06:45 | `inbox-triage`, morning pass | Weekdays |
| 07:00 | `morning-brief` | Weekdays |
| 07:05 | `decision-brief`, review pass | Monday |
| 07:15 | `weekly-review` | Monday |
| 07:30 | `chase` | Thursday |
| 15:30 | `inbox-triage`, afternoon pass | Weekdays |
| 16:00 | `end-of-day-close` | Weekdays |

The order matters more than the clock times. The sweep and the morning triage pass run before the brief so their output can appear in it. The connection check runs before both so the registry is current when they read it, and the health check runs after it for the same reason. The weekly review runs after the brief so it is not the first thing the leader sees on a Monday, and the decision review runs between the two, because the weekly review is the surface that renders what it finds.

On ChatGPT the order buys less than it looks. The sweep and the morning triage pass print into a chat instead of writing into the folder, so the 07:00 brief reads neither of them and builds the day from the calendar, the ledger, and mail alone. Two honest options. Move both jobs to a time the leader is awake and have them paste the commitment lines before the brief runs, which costs the leader ten minutes every morning. Or leave the clock as it is, accept a thinner brief, and say so at handover rather than letting it read as a bug. Pick one in the session and write down which.

If a brief arrives and the leader has already heard everything in it from other people, the schedule is too late. Move it earlier before you change anything else in the system.

---

## The four that do not get scheduled

`onboarding`, `meeting-prep`, `transcript-to-actions`, and `recall` are not on this list, and adding them is a mistake worth naming.

Each of them needs a subject that only a person can supply. Meeting prep needs to know which meeting. Transcript to actions needs to know which call. Onboarding needs a leader in the room answering six questions. Recall needs the question.

The scheduled jobs cover the first three anyway. The sweep runs transcript-to-actions across yesterday's meetings without being asked, and the morning brief offers meeting prep when a high-stakes meeting has none. Nothing covers recall, and nothing should. It exists for the moment the leader asks.

**`decision-brief` is the exception, and it is worth naming why.** On demand it needs the decision, which only the leader has. On its Monday pass the file supplies the subject itself. A review date that has passed is a subject. A condition that has fired is a subject. Two jobs, one behaviour, and section 9 schedules the second.

---

*Created by The NoW of Work. MIT licensed. Yours to edit, adapt, and rename.*
