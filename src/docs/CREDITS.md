# Credits and permission

## Who made this

**The AI Chief of Staff was created by The NoW of Work.**

[www.nowofwork.com](https://www.nowofwork.com)

The design, the behaviours, the approval gates, the capability registry, and the writing are ours. We built it because most AI assistants either do too much without asking or produce output nobody reads. This one is deliberately narrow: it drafts, it stays short, and it tells you when it cannot see something.

---

## What you are allowed to do with it

Everything, more or less. This is MIT licensed, which is about as permissive as software licences get. In plain language:

**You may:**

- Use it, for yourself or inside your organization.
- **Edit any file in it.** That is the point. The behaviours are written as instructions in plain markdown precisely so that a non-programmer can open one and change how it works.
- Adapt it for a client, a team, or a different industry.
- Rename it, rebrand it, and put your own name on your version.
- Charge money for work you do with it, or for a version you have built on top of it.
- Redistribute it, forked or unchanged.

**You must:**

- Keep the `LICENSE` file with any copy you distribute. That is the one legal requirement, and it is the whole of it.

**We would appreciate, though it is not required:**

- A line somewhere saying the original came from The NoW of Work.
- A note back to us if you build something interesting with it. We like knowing.

**Nobody is claiming:**

- That it will work for your situation. It ships as-is, with no warranty. Read the operating manual before you trust it with anything that matters, and keep the approval gates in place.

---

## What to change first

If you are adapting this, these are the files that make it yours, in order:

1. **`src/workspace/_manual.md` section 6.** The voice rules. Change these to your house style and every draft the system produces changes with them.
2. **`src/workspace/_manual.md` section 3.** The approval gates. Add one whenever someone says "never do that again."
3. **`src/behaviours/*.md`.** The behaviours themselves. Each one is a single markdown file with a trigger, a reading order, an output structure, and its own rules. Nothing is hidden.
4. **`src/docs/READ-ME-FIRST.md`.** The install guide your own clients will read.

Then run `python3 build/build.py` and both the Claude and the ChatGPT versions come out matching.

Do not edit anything in `dist/` or `plugin/skills/`. Those are generated, and the next build overwrites them.

---

*The Future is NoW.*
