#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes a single-line review of Monday to ``/output/entry.txt``
(override locally with ``ENTRY_OUTPUT_PATH``).

The review is assembled from four beats of one bad booking — the
verdict, the meeting, the inbox, and the coffee — closed by the
punchline that the reviewer is somehow booked again next week.
Each beat names a concrete Monday detail, so the line reads as a
review of a real Monday rather than a generic tiredness joke.
"""
import os
from pathlib import Path

# One beat per grievance; joined they form a single breathless review.
BEATS = [
    "Monday gets one star:",
    "a 9 a.m. meeting that could've been an email,",
    "214 emails that couldn't,",
    "coffee that quit before I did",
]

CLOSER = "\u2014 and somehow I'm booked again next week."


def render() -> str:
    """Return the review as one line of plain text."""
    return " ".join(BEATS) + " " + CLOSER


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
