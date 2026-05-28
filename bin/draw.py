#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = ["typer"]
# ///
"""Live drawing demo for kids: one rule, surprising patterns."""

import tkinter
import turtle

import typer

app = typer.Typer(
    help="Live drawing demos. Pick a command, watch a window open.",
    no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)

COLORS = ["cyan", "magenta", "yellow", "lime", "orange", "white"]

# Exceptions raised when the user closes the window during or after drawing.
# turtle and Tk each have their own — catch all of them as clean exits.
_WINDOW_DIED = (turtle.Terminator, turtle.TurtleGraphicsError, tkinter.TclError)


def _label_window(label: str):
    """Set up the window: black background, titled, and with the same label
    written in the top-left corner so multiple runs (open in separate
    terminals) are easy to tell apart side-by-side."""
    screen = turtle.Screen()
    screen.setup(width=900, height=700)
    turtle.bgcolor("black")
    turtle.title(label)
    scribe = turtle.Turtle()
    scribe.hideturtle()
    scribe.penup()
    scribe.color("white")
    scribe.goto(-screen.window_width() // 2 + 20, screen.window_height() // 2 - 40)
    scribe.write(label, font=("Helvetica", 14, "bold"))


def _wait_for_close():
    """Show the user how to dismiss the window, then block until they do."""
    print("\nDone drawing. Close the window or press Ctrl+C here to exit.")
    try:
        turtle.done()
    except (*_WINDOW_DIED, KeyboardInterrupt):
        pass  # window close or Ctrl+C — both are advertised exits above


@app.command()
def geometry(angle: float = 91.0, steps: int = 200, scale: int = 2):
    """Spin at one angle, drawing as you go.

    Implementation: a single turtle marches forward `i * scale` pixels (so each
    line is a touch longer than the last), then turns left by `angle` degrees.
    Repeats for `steps` iterations, cycling through COLORS. When `angle` divides
    360 evenly (90, 60, 72, 120…), the path closes into a regular polygon
    expanding outward; when it doesn't (91, 7, 144…), it never quite closes,
    producing rosettes, slow coils, and spirograph-like patterns.

    Interesting --angle values to try:

    * 90 — square (the boring baseline)
    * 91 — slow tilted coil; same code, one degree off
    * 60 — triangle expanding outward
    * 72 — pentagon
    * 120 — triangle, rotating the other way
    * 144 — five-pointed star (pentagram)
    * 7 — delicate flower / rosette
    * 170 — tight zig-zag that almost becomes a straight line
    """
    _label_window(f"geometry  angle={angle}  steps={steps}  scale={scale}")
    pen = turtle.Turtle()
    pen.speed(0)
    turtle.bgcolor("black")
    for i in range(steps):
        pen.color(COLORS[i % len(COLORS)])
        pen.forward(i * scale)        # each line is a touch longer than the last
        pen.left(angle)               # the one number that controls everything
    _wait_for_close()


@app.command()
def spiral(
    count: int = typer.Option(10, "-n", "--count", help="how many Fibonacci curves to draw"),
    scale: int = 12,
):
    """The Fibonacci golden spiral: each curve is the two before it added together.

    Implementation: maintains (a, b) = (0, 1) and advances `a, b = b, a + b`
    each iteration to walk the Fibonacci sequence. For each new value, draws
    a quarter circle of radius `a * scale` via turtle.circle(r, 90), which
    also rotates the turtle 90° so the next arc continues from the right
    place at the right heading. Consecutive Fibonacci ratios converge to the
    golden ratio φ ≈ 1.618, so the chained quarter-arcs trace the golden
    spiral — the same shape found in nautilus shells, sunflower seed heads,
    hurricanes, and spiral galaxies.

    Interesting flag combos to try:

    * (defaults) — the classic golden spiral, fits the window
    * -n 6 — just the inner coil, compact
    * -n 8 — small but with the full spiral feel
    * -n 12 --scale 15 — larger, fills the window edge to edge
    * --scale 8 — tighter coil, more visible inner detail
    * --scale 20 — dramatic; large outer arcs may push past the canvas
    * -n 14 — continues into a second outer loop (most will be off-screen)
    """
    _label_window(f"spiral  count={count}  scale={scale}")
    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(3)
    turtle.bgcolor("black")
    a, b = 0, 1
    for i in range(count):
        a, b = b, a + b               # the Fibonacci rule, hidden in plain sight
        pen.color(COLORS[i % len(COLORS)])
        pen.circle(a * scale, 90)     # a quarter-circle of radius = Fibonacci number
    _wait_for_close()


if __name__ == "__main__":
    try:
        app()
    except _WINDOW_DIED:
        pass  # window closed mid-draw — ops on a dead canvas raise these;
              # treat as a clean exit, not an error worth a traceback
