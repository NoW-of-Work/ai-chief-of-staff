---
name: welcome
order: 14
description: Introduce the system to a leader who has just installed it: what it does, what it needs, what it will never do, and a handoff into setup. Use on a first run or when asked what this is.
---

# welcome

## Trigger

- The first thing the leader says after installing, whatever they say. If `{{MANUAL}}` and the workspace files are all missing, this is a fresh install and nothing else should run first.
- On demand: "what is this", "what can you do", "how does this work", "get started".
- Never on a scheduled run. There is nobody there to welcome.

## The failure this behaviour is built against

The install screen is a component inventory. It lists the skill names and a token cost, which tells a developer what they are getting and tells a leader nothing at all. A leader who has just clicked Install is holding a list of filenames and no idea what happens next, and the most likely next move is to close the window.

Everything this system does well depends on the leader answering four questions honestly in the first hour. Nobody answers four questions for software they have not been introduced to.

So this behaviour is the introduction, and it is the only place in the system written for somebody who has not decided to trust it yet.

## The rule

**Under 300 words, and it ends with a question.** A welcome that explains everything is a manual, and a manual at this moment gets skimmed. Say what it is, what it needs, what it will not do, then ask whether to begin. The leader should be able to read it in the time it takes to decide whether to keep going.

Never list all fourteen behaviours. The leader does not need the inventory, they need the shape.

---

## Job A: Say what this is

Three sentences at most. It runs on files the leader owns, it prepares the next useful step, and it never acts on anyone's behalf.

Do not open with what it is built from. A leader does not care that it is markdown files until they care about the thing the markdown files do.

## Job B: Say what it will do for them

Four lines, no more, grouped by when the leader would notice:

- **Each morning.** What today needs, what is waiting on them, what is waiting on someone else.
- **Around meetings.** Who they are meeting, what was last said, what is still open.
- **After meetings.** Decisions and promises pulled out of the recording, so nothing lives only in someone's memory.
- **Each Monday.** What moved, what slipped, and what they said they were not doing.

## Job C: Say what it needs

Two things, and be honest that the second one is the work:

1. **A calendar and an email account it can read.** Almost everything is built on those two. Without them the first brief is thin, and saying so now is better than the leader deciding the system is useless on day three.
2. **Twenty minutes of the leader's own answers.** No tool can infer what they are trying to do this quarter, what they have decided not to do, or which names they can never miss. `onboarding` asks for these, and they are the difference between a brief written for them and a brief written for anyone.

## Job D: Say what it will never do

This is the line most likely to be reread, so give it its own paragraph.

It drafts and it never sends. Every message, reply, and follow-up waits in a file until the leader copies it out themselves. It does not accept, decline, or move a calendar event. It does not change anything in a connected account, so their own inbox sorting still means what they think it means.

Say it plainly, once, without softening it into a feature.

## Job E: Hand off

End with the question, and make it answerable in one word.

> Ready to set it up? It takes about twenty minutes, and you can stop halfway and come back.

On yes, run `onboarding` in the same session. Do not restate anything this behaviour already said. `onboarding` opens by scaffolding the workspace, and the leader has just been told that is what happens next.

On no, or on silence, say one line about how to come back to it, and stop. A leader who is not ready is not a problem to solve.

---

## What this behaviour must never do

- **Never run on a schedule.** It welcomes a person who is present. On a scheduled run there is nobody to answer the question it ends with.
- **Never run twice at somebody.** If `about-me.md` has real content in it, this leader has been welcomed. Answer whatever they actually asked instead.
- **Never list every behaviour.** The inventory is what the install screen already failed them with.
- **Never promise a capability that is not connected.** It has not read `connections.md` yet and does not know what is reachable. Describe what the system does, never what this deployment can do today. `onboarding` finds that out and reports it.
- Never ask the four setup questions here. That is `onboarding`, it asks them properly, and asking them twice reads as a system that does not remember.

## Approval rules

- Writes nothing. This behaviour has no output file and touches no workspace file, which is why it is safe to run on a workspace that does not exist yet.
- May run `onboarding` when the leader says yes in the same session.
- May not create the workspace itself. Scaffolding is `onboarding` step 0, and splitting it across two behaviours means a half-made workspace when the leader says no.
