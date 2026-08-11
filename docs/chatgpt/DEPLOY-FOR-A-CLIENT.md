# DEPLOY FOR A CLIENT

**AI Chief of Staff, v1.2.0. Created by The NoW of Work.**

This is the runbook for installing the system for somebody else. It assumes you have read `READ-ME-FIRST.md` and can already do the install on your own machine.

`READ-ME-FIRST.md` tells a leader how to set this up for themselves. This file tells you how to set it up for a leader who will not read that file, in one sitting, and have it still running in a month.

---

## 1. Confirm before the session

Do all of this by email, days ahead. A session that stalls at minute twelve waiting on an IT ticket does not recover.

| What to confirm | Why it matters | If the answer is no |
|-----------------|----------------|---------------------|
| Which AI tool the leader pays for, personally or through the company | The system runs inside Claude or ChatGPT. There is no third option and no standalone app | Stop. Get the subscription first. Do not book the session |

| On ChatGPT, which plan | The plan caps active scheduled tasks: 3 on Go, 5 on Plus, 10 on Business and Edu, 15 on Pro and Enterprise. The finished clock is ten. Find this out now, not in week three when a task refuses to save | Plus is a five-job deployment and that is a legitimate one. Decide which five before the session and say so at handover. Go stalls in week two |

| Whether the account is a personal one or an enterprise seat | Enterprise seats often have connectors switched off at the tenant level | Find the admin now, see the row below |
| Calendar connected, and email connected | Almost everything is built on those two | You can still run the session, but say up front that the first brief will be thin |
| Where the workspace folder will live | You will not be there at 06:30 on a Tuesday to open the laptop for it | Cloud storage the leader owns. Insist on this one |
| Who can grant connector access | In most organizations of any size, it is not the leader | Get that person's name and a slot in their week, before your session |
| Whether an assistant manages the calendar | The system will start commenting on how the calendar is built. That is somebody's work you are grading | Bring the assistant into the session, or brief them separately first |
| Sixty minutes with the leader, not with a delegate | The four answers in section 4 cannot be given by anybody else | Move the session. A delegate produces a workspace nobody reads |

### On the folder location

Say this plainly and do not let it slide. The workspace has to sit in cloud storage the leader controls, at the top level, named `ai-chief-of-staff`.

Two reasons. A scheduled morning brief has to run at 06:30 whether or not a laptop is open. And a laptop dies, gets replaced, or goes in for repair, and the leader's working memory should not go with it.

If the organization blocks personal cloud storage, use the corporate one. What matters is that a scheduled task can reach it and the leader can open it on a phone.

**On ChatGPT this is stricter than it looks.** A scheduled task cannot read the files attached to a project, including the project it was created in, so uploading the workspace to the project does not make it reachable at 06:30. The folder has to sit in a connected app, and the prompt has to name that app. `READ-ME-FIRST.md` Path C step 5 is the step, and it leaves two copies to keep in step, which is worth saying at handover rather than discovering in week three.

If the leader will not connect an app, say the honest thing in the session: ChatGPT cannot run this unattended. What you can leave behind is a trigger-only task that says "it is 07:00, run the morning brief," with the leader running the real prompt inside the project by hand. Do not install a full schedule that quietly produces context-free output every weekday.

---

## 2. The consent conversation

Setup reads about twenty of the leader's own sent emails, four weeks of their calendar, the titles of their recent documents, and six weeks of email subject lines.

You are about to point a tool at a stranger's sent folder on their own account. Somebody has to say it out loud, to them, before it happens. That somebody is you.

Say it in the session, before you run onboarding, in roughly these words:

> Before I start this, here is exactly what setup reads. It reads fifteen to twenty emails you have sent, so it learns how you write and can draft in your own voice. It reads the last four weeks of your calendar, so it works out your rhythm on its own and spares you twenty questions about it. It reads the titles of your recent documents and six weeks of email subject lines, so it can guess what you are working on and you can correct the guesses. It will not open a thread somebody sent you unless you point it at one. Nothing gets sent to anyone. Are you comfortable with that?

Then stop talking and wait for an answer.

Setup is not the whole story, and week three is where the scope widens. `inbox-triage` reads new mail as it arrives, twice a working day, from the week you schedule it. Say that in the same breath as the script. A leader who consented to twenty sent emails and finds a daily read of their inbox in week three has been told the truth once and then had it quietly changed on them. If you would rather split it, say the second half again in the session where you add triage, and write the date you said it into the handover page.

The question that comes back is almost always the same one: what can it do without asking me.

**It drafts. It does not send.** Say what it may do without asking: read, summarize, write into the workspace folder, draft a reply and hold it. Say what it may never do: send mail, move a calendar entry, post a reply, authenticate anything, save `tomorrow.md` without a yes, close a commitment without a source to point at, or write anything personal about a named person into `people/`. It may create the person file. What goes in it needs the leader's yes, every time. If it ever offers to connect a tool for the leader, that is a defect and section 6 says so.

### If the answer is no, or a hesitation

A hesitation is a no. Treat it as one and move on without making it awkward.

The system still works. You lose the inferred voice profile and you replace it with a stated one, which is thinner but more honest, because the leader confirmed it.

Ask for three bullets instead:

1. "Do you greet people in internal email, or do you open with the point?"
2. "How do you sign off, word for word?"
3. "Name two phrases you would never write."

Write those into `about-me.md` section 3 as confirmed values, not as `(inferred)`. The greeting habit and the sign-off go under **How I write**. The two phrases go under **How I do not write**. Then tell the leader what they gave up: drafts will need more editing for the first two weeks, and correcting those drafts as they arrive is what closes the gap.

### The partial yes

The most common answer is "calendar yes, mail no." Take it. The calendar carries the working rhythm, the meeting cadence, and the key relationships, which is most of the value in the auto-fill step. Record Email as `missing` in `connections.md` so no behaviour quietly assumes it, and revisit in a month.

---

## 3. The sixty-minute session

Sixty minutes, in eight blocks. The agenda is tight because the middle of it is the part that matters and you want the time.

| Minutes | Block | What you are doing |
|---------|-------|--------------------|
| 0 to 5 | Access and folder | Confirm the subscription, create the folder in cloud storage, confirm calendar and mail respond |
| 5 to 10 | Consent | Section 2, out loud. Wait for the answer |
| 10 to 15 | Install | Path C from `READ-ME-FIRST.md`. Silent work, so talk through what happens next while it runs |
| 15 to 30 | Onboarding, steps 0 to 5 | Steps 0 to 2 are silent. At step 3 the leader reads the confirmation block and you take corrections. Step 4 asks its six clusters, step 5 saves behind an approval gate and hands off to `health-check`. Read that verdict before you move on |
| 30 to 45 | The four questions, in depth | Section 4. Onboarding already asked four of these once. This is where you get the real answer |
| 45 to 52 | First brief | Run it, read it together, ask what is wrong with it |
| 52 to 58 | Schedule | The morning brief only. See `SCHEDULES.md` |
| 58 to 60 | Handover | What happens tomorrow, and the one thing they have to do |

### What you do while the leader reads

Minutes 15 to 30 are the only quiet stretch, and it is easy to waste them. The leader is reading a block of roughly fifteen fields, grouped, with `[ok / fix]` beside each one and `(inferred)` on everything the system guessed.

Three jobs while they read.

**Write corrections down word for word.** When the leader says "no, Priya is a client, not a report," type "client" into the fix, not "external stakeholder." Your paraphrase is a second guess layered on top of the first one.

**Watch for hesitation, and name it.** A leader who pauses over a field and then says "yeah, fine" has not confirmed it. Say "you paused on that one." The pause is worth more than the word.

**Count the corrections.** If the leader gets to the bottom of the block having corrected nothing, they were being polite. Go back to the top and pick the two fields you are least sure of, and ask about those specifically. A block with zero corrections is a workspace built entirely on guesses.

### The first brief

Run it in front of them. Then ask one question: "What is wrong with this?"

Do not ask whether they like it. Fix whatever they name by editing the source file, in front of them, right there. That single demonstration is what teaches the leader the whole operating model. The output is disposable. The files are the product.

**There will be nothing about connections in the first brief.** That is correct, and worth pointing out, because it looks like something is missing. The system just started its own timers.

---

## 4. The four questions

Anything still in `[BRACKETS]` after onboarding is a decision nobody has made. Most of them can wait. Four cannot.

| Question | Where it lands | What it changes |
|----------|----------------|-----------------|
| What do I flag every single time, even on a busy day | `about-me.md` section 6 | Whether the brief surfaces the thing that mattered |
| What must I never do | `about-me.md` section 8 | Whether the leader trusts it enough to keep using it |
| What is this quarter actually for | `my-work.md` section 1 | Whether priorities read as real or generic |
| What are you not doing right now | `my-work.md` section 5 | Whether the weekly review is worth reading |

### How to get a real answer rather than a polite one

**Always flag.** Do not ask for a category. Ask for a name. "If one person's email arrived at eleven on a Friday night, who would you want to know about before Monday?" Then ask for two more. Names are testable. "Key stakeholders" is not.

**Hard stops.** Ask what would embarrass them. "What is the thing that, if this drafted it and you sent it without looking, would cause you a real problem?" You will usually get a category of information. That is the more useful answer.

**This quarter.** Ask for the counterfactual. "If the quarter ended tomorrow and exactly one thing had moved, which one makes it a quarter you are happy with?" If the leader names three, ask which one they would keep. A priority list where everything is first is a list the system cannot rank.

**What you are not doing.** This is the one leaders resist, and they resist it for a good reason. Saying it out loud makes it real, and it usually names a project somebody they like is running.

Four ways through it, in the order to try them.

1. **Make it a calendar question.** "A stranger reads last week's calendar. What do they conclude your top priority is, and why are they wrong?" This gets an answer almost every time. It asks about a document, and a document is easy to be honest about.
2. **Ask for the thing that keeps coming back.** "What lands on your desk every couple of weeks that you keep half-doing?"
3. **Offer a suspect.** Name something you saw in the calendar during onboarding. "There are four hours a week on the website redesign. Is that this quarter's work?" Leaders will correct a wrong guess faster than they will volunteer a right one.
4. **Take one item and stop.** One named thing beats a category. "The website redesign is not this quarter" gives the weekly review something to check against. "Being more focused" gives it nothing.

Then close the loop out loud: "I am going to have it flag these when they show up in your week. Say the word and I will take them off the list." Consent to be told about drift is what makes the drift check land in week three. Without it, the same line reads as a scold.

---

## 5. Success criteria

Observable, not aspirational. Each of these is something you can open a folder and point at.

### Day 1, before you leave the session

- Seven files exist in the workspace. Four carry the leader's own answers: the manual, `about-me.md`, `my-work.md`, and `connections.md`. Three still hold only their templates, and on day one that is correct: `decisions.md` because no call has been closed yet, `commitments.md` because nothing has been captured yet, and `tomorrow.md` because `end-of-day-close` is what drafts it and that does not go on the schedule until week four.
- No row in `connections.md` still reads `unknown`.
- One brief exists, under 400 words, and it does not open with a greeting. In Claude it is in `briefs/`. In ChatGPT it is printed in the chat unless a storage connector is already live, in which case it writes there and asks first.
- Exactly one scheduled task exists. Not the whole ramp.
- The leader corrected at least three fields during the confirmation block.
- All four answers from section 4 are written into the files, in the leader's words.

That last pair are the ones people skip. If corrections were zero, or the four answers came out as one-word abstractions, the session is not finished. Take the extra ten minutes.

### Day 7

- Five briefs, one per working day. In Claude they sit in `briefs/`, and a gap means a scheduling problem that section 6 will name. In ChatGPT the run prints into the chat and `briefs/` stays empty by design, so count five scheduled runs in the chat history instead, and read a gap as a paused task rather than a missing file.
- At least two source files have been edited since setup, by the leader, without you asking.
- Fewer `(inferred)` labels than there were on day 1.
- The leader can name one specific thing a brief told them that they would otherwise have missed. Ask for it. Accept a real example only.
- At least one line in the `connections.md` change log.
- No capability nudges have fired. That is the system working, not the system asleep.

### Day 30

- `commitments.md` has entries in both directions, and the `Closed (this quarter)` section has at least one entry. `archive/` is still empty, and it should be. Nothing moves there until it has been closed 90 days, so an empty `archive/` at day 30 is the rule holding, not a gap.
- `people/` has a file for every name on the always-flag list.
- Seven behaviours on a schedule, following the ramp in `SCHEDULES.md`, each one still being read. `health-check` is the eighth, and it goes in ahead of this check-in because its verdict is what you read the folder against. Count entries in the Scheduled panel and you should find nine, not eight: `inbox-triage` runs twice a day and takes two tasks. Eight behaviours, nine entries. Anything past nine means something was installed twice, and anything short of nine means a job you think is running is not. On ChatGPT, nine entries is already over the Plus cap of five, so a leader on Plus should be at five by design and you should know which four you left off.
- `decisions.md` holds at least one `Made` entry, and each of its two conditions under **Would change my mind** carries a date or a checkable signal. "If things change" is not a condition and the behaviour will not accept it.
- `tomorrow.md` gets approved most evenings rather than ignored.
- The weekly review has produced at least one decision the leader acted on. Chasing a stale commitment counts. Dropping one counts. Defending a protected block counts.
- The leader has told the system it was wrong about something in the last seven days.

That last one is the real measure. A leader who never corrects it has stopped reading it.

---

## 6. When it goes wrong

The leader sees a symptom. You can see the cause, because you know where the files are and what the build does. This table is written for you.

| What you see | What it actually is | What to do |
|--------------|---------------------|------------|
| The brief runs long, or opens with "Good morning" | The operating manual is not in context. In Claude, the session is outside the project. In ChatGPT, the custom instructions were truncated on paste | Reopen inside the project. In ChatGPT, re-paste and check the field did not silently cut at its character limit |
| Priorities read generic | `my-work.md` section 2 is empty or still bracketed, so there is no ranked list to draw from. If section 2 is filled and priorities still read generic, section 1's strategic priority is an abstraction | Fill section 2 first, capped at five. Then go back to question three in section 4 and ask for the counterfactual version |
| The drift check never says anything | `my-work.md` section 5 is empty. The system has nothing to check against | Section 4, question four. Use the calendar framing |
| It reads files but cannot save them | Write access was never granted on the storage connector. Read and write are separate scopes on most of them | Re-grant with write enabled. Test by asking it to append one line to `commitments.md` |
| `(not connected)` about the calendar | Either the token expired, or an admin revoked the grant across the tenant. Those look identical from inside the chat | Have the leader reconnect. If it fails again within a week, it is the admin, and you need the person from section 1 |
| A scheduled task produces nothing useful | Almost always one of two things. The folder is on a laptop, or the prompt does not name the folder | Check the prompt text against `SCHEDULES.md`. Every block there names the folder for exactly this reason, and every block leaves `[WHERE THE WORKSPACE LIVES]` for you to replace with the real home before you paste |

| A ChatGPT scheduled brief arrives on time and reads like it has never met the leader | The prompt points at the project. A scheduled task cannot read project files, so the run had no workspace at all and wrote a generic day from nothing. It looks like a working job, which is why it survives for weeks | Move the workspace into a connected app, `READ-ME-FIRST.md` Path C step 5, and re-paste the ChatGPT block from `SCHEDULES.md` with that app named in the first line |

| The transcript sweep produces nothing, every day, and the `Transcripts` row says `missing` | Designed behaviour. The capability is not there and every job that needs it exits silently | Nothing. Say so at handover before the first silent week reads as a broken job |
| The transcript sweep produces nothing, and the `Transcripts` row says `connected` | The capability is `failing`. The row is stale, and every behaviour reading it is treating an empty result as a quiet week | Run `connection-check`. It probes by use and rewrites the row. If it comes back `connected` again and the sweep stays silent, that is a defect, not a setting |
| A brief mentions the same missing tool twice in two weeks | The nudge dates in `connections.md` are not being written back, usually because write access is read-only | Same fix as the write-access row. Then say "not now" twice to silence it while you sort it out |
| The Monday decision pass never surfaces anything | Usually correct. Most Mondays nothing has come due. If `decisions.md` still holds no `Made` entry after a month, the leader is deciding and not logging | Ask what they closed last week. Run `decision-brief` against it and log the entry in front of them, once |
| The leader says it is "fine" and cannot name anything it got wrong | Nobody is reading it. This is the quiet failure and it is the serious one | Run `health-check` first. It reads the files, tests what it can reach, and gives one verdict. Then section 7 |
| It invents a meeting detail, a date, or a quote | A defect, not a setting. No amount of file editing fixes it | Note the exact line, the behaviour, and the version. Open an issue |
| It offers to connect or authenticate something | Same. It is never permitted to authenticate anything | Note it and open an issue |

Two rows deserve a sentence of their own. `missing` and `failing` look the same to the leader and they are different problems. A missing tool is a gap the leader already knows about. A failing tool is a gap they do not know about, because they still think it is running. Only one of those is urgent, and it is the second one.

---

## 7. Handover

### What you leave behind

- The workspace folder, in cloud storage the leader owns, with the leader-owned files filled in.
- The exact prompt text for every scheduled job, in writing, from `SCHEDULES.md`. Not a description of the prompt. The text.
- One page with the four questions and the answers the leader actually gave, in their words. This is what you re-read at the 30-day check-in.
- The name of the person who grants connector access, and what they granted.
- A booked 30-day check-in. Book it in the session. It does not happen otherwise.

On ChatGPT, two more things go in that handover. The workspace exists twice, once in the connected app for the scheduled runs and once in the project for the sessions the leader opens, and a scheduled run prints its output for pasting rather than writing it back, so the leader is the thing keeping the two in step. Tell them to paste into the connected folder first, because that is the copy tomorrow morning reads. And say the plan's task cap out loud, with the number of jobs you actually installed against it.

### What the leader owns

Five files, and nobody else writes them: `about-me.md`, `my-work.md`, `tomorrow.md`, `commitments.md`, `decisions.md`.

The last one has a rule worth saying at handover. The system drafts an entry after the leader decides, and it never writes an outcome the leader has not stated. Once an entry reads `Made`, the reasoning in it is never edited, including where it turned out to be wrong. That is the point of the file.

The system owns `connections.md` and keeps it current. The folders fill themselves.

Say this in one sentence at handover: the output is disposable, the five files are the product, and the way to make next week better is to correct a file rather than to argue with a brief.

### The honest note

Here is the failure mode that does not announce itself.

Everything runs. Briefs arrive every morning. The folder fills up. Nothing errors. And nobody has edited a source file in three weeks.

That means the leader is not reading the output. The deployment has failed, quietly, and it will keep looking healthy for months.

Check this at 30 days by running `health-check`. Read the verdict, then open `about-me.md`, `my-work.md`, `commitments.md`, and `decisions.md` and look at the modified dates yourself. If none has moved since setup, do three things.

1. **Remove behaviours. Do not add any.** Go back to the morning brief alone, and say why out loud: the ones you are switching off were never the problem.
2. **Re-ask the four questions.** A generic answer in week one produces a generic brief in week four. A generic brief is one nobody misses.
3. **Ask the leader when they read it.** Usually the answer is that the brief arrives at 06:30 and they open their laptop at 08:45, by which time they have already been told everything in it. Move the schedule. That one fix has saved more deployments than every other item in this file.

A system that gets corrected is working. Silence from the leader is not approval.

---

*Created by The NoW of Work. MIT licensed. Yours to edit, adapt, and rename.*
