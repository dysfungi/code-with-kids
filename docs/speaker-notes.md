# Speaker Notes & Runbook

Audience: 3rd–5th graders (~8–11 y/o). Two identical sessions (reuse content).
Centerpiece: drive a turtle script live. One knob, surprising shapes; payoff is the
Fibonacci spiral hiding everywhere in nature.

---

## Timing table

| Beat | Target | Cut if squeezed |
|------|--------|-----------------|
| Hook (square → coil) | ~1 min | never |
| Kids drive the geometry | ~3–4 min | trim to two angles |
| Fibonacci spiral + reveal | ~2–3 min | never (the payoff) |
| Close (humans notice) | ~1 min | never (the whole point) |
| **Total** | **~10–12 min** | **~6 min minimum** |

Q&A will likely eat the back half. Front-load the geometry play — those moments
generate the best questions.

---

## Pre-talk checklist

- [ ] `chmod +x bin/draw.py` (one-time)
- [ ] `./bin/draw.py --help` — confirms `uv` resolves `typer` and both subcommands list
- [ ] Run **each** of the kid-favorite shapes once so the window opens fast on stage:
      ```bash
      ./bin/draw.py geometry --angle 90
      ./bin/draw.py geometry --angle 91
      ./bin/draw.py geometry --angle 144
      ./bin/draw.py geometry --angle 7
      ./bin/draw.py spiral
      ```
- [ ] **Test on the projector**, not just your laptop. The turtle window pops up at the
      OS level; confirm it's big enough and the colors (cyan / magenta / yellow / lime
      on black) read from the back row.
- [ ] Open Claude Code (`claude`) once in the repo so its first launch on stage is fast.
      `.claude/settings.json` is permissive, so no approval prompts mid-demo.
- [ ] Have an editor pane open showing `bin/draw.py` — the kids should be able to *see*
      the code being edited.
- [ ] **Test school wifi.** Hotspot ready as backup (the AI step needs internet;
      `./bin/draw.py` itself does not).
- [ ] Pull up the [slide deck](https://docs.google.com/presentation/d/1h-PvlVTlIiLPIK3bq5QUkgVuotW2uy6fhOv5R0lFleY/edit)
      in presenter mode in a separate window before walking on stage.

---

## Beat 1 — Hook (~1 min)

**Say:**
> "I'm going to draw a shape. Watch."

Run:
```bash
./bin/draw.py geometry --angle 90
```

A square spirals out (each step longer than the last, but always turning 90°). Boring.
The kids get it.

**Say:**
> "Square. Easy. Now watch what happens if I change ONE number."

Re-run with `--angle 91`:
```bash
./bin/draw.py geometry --angle 91
```

The shape slowly tilts and coils into a hypnotic flower-like pattern. *Pause.* Let it
land.

**Say:**
> "Same code. Same rule. One degree different."
> "Want to pick your own?"

---

## Beat 2 — Kids drive the geometry (~3–4 min)

**Say:**
> "Shout a number between 1 and 359. We'll try a bunch."

Take their first number. Run it. (Pre-warmed favorites if they freeze:)

| Angle | Shape | Cue |
|---|---|---|
| `90` | square (boring baseline) | "we know this one" |
| `91` | slow tilted coil | "ohhh" |
| `60` | triangle expanding | "what's special about 60?" |
| `72` | pentagon expanding | "five-sided!" |
| `120` | triangle, other way | "still three sides — why?" |
| `144` | pentagram | "FIVE-POINTED STAR" |
| `7` | flower / curl | "looks like a flower" |
| `170` | tight zig-zag | "tries to be a line but can't" |

After 2–3 shapes, ask the AI to extend (kids pick the change):

| Kid says | Prompt to Claude |
|---|---|
| "more colors!" | "In `bin/draw.py`, expand `COLORS` to about 10 distinct bright colors and use the same modulo cycle." |
| "make it faster!" | "Bump `steps` default to 400 and make `scale` 3 — keep the visual but bigger." |
| "thicker lines!" | "Set `pen.width(3)` in `geometry` so the lines are easier to see on a projector." |
| "two pens!" | "Add a second turtle drawing the mirror pattern (negative angle) at the same time." |

Re-run after each edit. Two extensions is plenty.

---

## Beat 3 — The Fibonacci payoff (~2–3 min)

**Say:**
> "Okay. There's one set of numbers that makes the most famous shape in math."
> "Watch."

Write the rule on the board / type it in the air:
> "1, 1, 2, 3, 5, 8, 13, 21…"
> "Each number is the two before it added together. That's the whole rule."

Run:
```bash
./bin/draw.py spiral
```

The golden spiral grows on screen, quarter-curve by quarter-curve.

**Say:**
> "Look at this shape. Remember it."
>
> "This **exact** spiral is hiding in a **seashell**."
> "It's the swirl in a **sunflower**."
> "It's the shape of a **hurricane** from space."
> "It's how a **whole galaxy** is shaped."
>
> *(pause)*
>
> "Same simple rule. Add the last two. Draw the curve. The universe is doing this
> everywhere, and nobody told the sunflower."

Optional re-run, bigger:
```bash
./bin/draw.py spiral -n 12 --scale 15
```

---

## Beat 4 — Close (~1 min, never skip)

**Say:**
> "Last thing — here's what I really want you to remember."
> "The computer drew every one of those in a second. Easy for it."
> "But it took a *curious human* — 800 years ago, named Leonardo of Pisa — to *notice*
> the pattern was there."
> *(pause)*
> "Tools keep changing. When I started, I wrote code by hand. Now an AI helps me.
> In ten years it'll be something else again."
> "Noticing things. Wondering why. Picking what to try next."
> "**That part is still you.**"
> *(beat)*
> "...questions?"

---

## Likely Q&A (crisp answers)

| Question | Answer |
|---|---|
| "How does the computer know how to draw?" | "It doesn't, really. We told it: go forward, turn this many degrees, draw a line. It just follows the rule super fast. That's all 'AI' is doing too — following rules, really fast." |
| "Why does the spiral show up in plants?" | "Plants are trying to pack seeds or leaves without overlapping. The golden-ratio spiral is the *most efficient* way to do that — so plants that grow this way win. Nature didn't pick it; it just worked." |
| "Will AI take everyone's jobs?" | "It changes the work, like calculators changed math class. The jobs that disappear are the ones where you just follow instructions. The jobs that grow are the ones where you decide what's worth doing." |
| "How do I learn to code?" | "Pick one tiny thing you want to make — a meme, a Minecraft helper, anything. Then ask 'how do I do *that*' over and over. Scratch (scratch.mit.edu) is the best starting point." |
| "Are you smart?" | "I'm curious, mostly. Smart is overrated. Curious wins." |
| "How much do you make?" | "More than enough. Software is a well-paying career and most engineers earn very comfortably." |
| "Did you always want to do this?" | "I liked building and breaking things. Computers are infinite Lego." |

---

## Recovery playbook

| Problem | Fix |
|---|---|
| Wifi down, AI won't connect | Skip the AI extensions. Just keep running `./bin/draw.py geometry --angle <N>` with kid-chosen numbers, then `./bin/draw.py spiral`. No network needed for the script itself. |
| `uv` can't resolve `typer` (rare) | The error will say so. Fallback: `pip install typer` then `python3 bin/draw.py …`. |
| Turtle window doesn't open / Tk missing | `brew install python-tk@3.13` (or whichever python). Test before you walk on stage — this is the #1 thing to verify on the actual machine. |
| AI produces broken code | Discard the edit and re-run the last known-good command. The committed `bin/draw.py` is your safety net. |
| Beat 1's first shape is unimpressive | Don't apologize — say "boring, right? watch THIS" and jump to `--angle 91`. |
| Kids ask for math you don't know | "I don't know — let's find out." Then ask Claude. Models the actual job. |

---

## Optional one-liner garnish (only during AI think-time, max 1)

Use only if the AI is thinking and there's a dead beat to fill. ~15 sec each:

- *(now)* "I count patterns for a living — I keep a video game online for millions of
  players. Most of my job is *noticing* when something's about to wobble, before it
  falls over. Same skill as today."
- *(college era)* "My college professor wrote code by hand on a projector. No colors,
  no autocomplete. He'd hate this."

One per session, max. The math is the star.
