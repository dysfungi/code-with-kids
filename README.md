# Let's Find a Pattern — a turtle-graphics talk

An elementary school talk for 3rd–5th graders (~10–12 min + Q&A).

**The hook:** one rule, surprising pictures. Change one number, get a square. Change it
again, get a flower. Change it again, get the same spiral that hides in seashells and
galaxies. The close: the computer drew it in a second — but a curious human had to
*notice* the pattern was there.

---

## Quick start

```bash
chmod +x bin/draw.py            # one-time
./bin/draw.py --help            # see both commands

./bin/draw.py geometry              # default angle=91 → slow coil
./bin/draw.py geometry --angle 90   # a square
./bin/draw.py geometry --angle 144  # a pentagram
./bin/draw.py geometry --angle 7    # a flower

./bin/draw.py spiral                # the Fibonacci golden spiral
./bin/draw.py spiral -n 12 --scale 15
```

The `uv run` shebang (line 1 of `bin/draw.py`) resolves `typer` automatically on first
run. `turtle` is part of the Python standard library, so nothing else needs installing.

Requirements: Python ≥ 3.11 and [`uv`](https://docs.astral.sh/uv/) on PATH.

---

## Slides

The talk's slide deck lives in Google Slides — open it for the talk, copy it to remix:

- [Google Slides source](https://docs.google.com/presentation/d/1h-PvlVTlIiLPIK3bq5QUkgVuotW2uy6fhOv5R0lFleY/edit)

If exported, the rendered snapshot belongs at `Slides.pdf` in the repo root.

---

## The four beats (~10–12 min, compresses to ~6)

1. **Hook (~1 min).** "I'm going to draw a square. Then change one number, and watch it
   stop being a square." Run `geometry --angle 90`, then `91`. Audible "ohh."
2. **Kids drive the geometry (~3–4 min).** They shout numbers (`144`, `72`, `60`, `7`)
   and call out edits ("more colors!", "make it faster!"). The AI extends the script
   live.
3. **The Fibonacci payoff (~2–3 min).** Show the rule `1, 1, 2, 3, 5, 8, 13…` Run
   `./bin/draw.py spiral`. Reveal: this same spiral hides in seashells, sunflowers,
   hurricanes, and galaxies.
4. **Close (~1 min).** The computer drew it in a second. A human had to *notice* it.
   Tools change; noticing doesn't.

Full runbook (timing, exact prompts, Q&A prep, wifi-down recovery):
[docs/speaker-notes.md](docs/speaker-notes.md).

---

## What's in the repo

| Path | What |
|------|------|
| `bin/draw.py` | The whole demo. Two `typer` subcommands (`geometry`, `spiral`), uv-managed deps inline. |
| `docs/speaker-notes.md` | Runbook — timing, beat-by-beat exact words, AI prompts, Q&A, recovery |
| `.claude/settings.json` | Permissive Claude Code permissions so the live AI demo doesn't stall |

---

## Disclaimer

Personal project. Personal views. Not affiliated with, endorsed by, or representing any
employer. No confidential or proprietary information is included.

---

## License

- **Code:** [MIT](LICENSE)
- **Presentation content** (speaker notes, narrative): [CC-BY-4.0](LICENSE-CONTENT) — reuse with attribution.
