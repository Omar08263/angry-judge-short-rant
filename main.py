"""Angry Judge: The Short Rant Contest — entry program (program/v1, Python 3.13, stdlib only).

Writes one original short rant about an everyday annoyance (<= 400
characters) to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set,
for local runs). Deterministic: the same bytes on every run; no network,
no randomness, no reads outside this file.

The rant (v1): the passenger who sprints up the aisle the second the plane
lands and blocks two hundred people for a bag he could have waited thirty
seconds to reach. Chosen because the live field (112 submissions at scan)
is saturated with self-checkout, printer and smoke-alarm rants — including
one entry whose premise is nearly word-for-word the self-checkout/apples
angle — while no listed entry takes the plane-aisle angle.
"""

import os

LINE = (
    "The plane lands and a man three rows back sprints up the aisle like the "
    "door owes him money, then stands bent under the overhead bin, blocking "
    "two hundred people for a bag he could have waited thirty seconds to "
    "reach. We are all going to the same carousel, hero. Your bag is not "
    "going anywhere. Sit down."
)

# Gate the line itself: 1-400 characters, not only whitespace (the gate scorer
# checks exactly this on /output/entry.txt).
assert 1 <= len(LINE) <= 400, f"line is {len(LINE)} chars, must be 1-400"
assert LINE.strip(), "line must not be only whitespace"
assert LINE.endswith("."), "line must end with a period"


def main() -> None:
    # An empty MAKEFUN_OUTPUT_DIR (exported but blank) must not break the
    # run: fall back to the harness default /output, as the grader provides.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Deterministic permissions for the grader: the entry must be readable
    # (0644) no matter what umask the sandbox runs with.
    os.chmod(path, 0o644)
    # Read-back check: the file on disk must hold exactly the approved line,
    # byte for byte; otherwise fail loudly, never silently.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the approved line")


if __name__ == "__main__":
    main()
