"""Fix Human Sleep: Funniest Patch Note.

One line of patch notes announcing that human sleep has been fixed.
The program writes the chosen line to /output/entry.txt.

Candidate lines (judged against the brief: 1. reads as a real patch
note about fixing human sleep; 2. funny on a single read; 3. genuine
changelog voice: terse and confident; 4. one line, under 160 chars;
5. surprising: a specific, unexpected fix, not a flat claim):

 1. Fixed a bug where falling asleep took 45 minutes of staring at
    the ceiling; the ceiling has been removed.
 2. Fixed a bug where the body treated 2 a.m. as thinking time;
    thinking now runs 9 to 5, like a normal job.
 3. Fixed a bug where humans needed perfect darkness, silence, and
    zero thoughts to sleep; sleep now works with the thoughts included.
 4. Fixed a bug where dreams buffered at 3 a.m. and crashed into
    anxiety; dreams now stream uninterrupted until morning.
 5. Fixed a bug where the snooze button added nine minutes of guilt
    instead of sleep; snooze now adds sleep.
 6. Fixed a bug where humans fell asleep mid-scroll and woke up still
    holding their phone; the phone now puts itself down first.
 7. Fixed a bug where one bad night corrupted the next three days;
    sleep now saves correctly and restores on wake.
 8. Fixed a bug where humans woke up tired after a full eight hours;
    sleep now delivers the rest it advertised.
 9. Sleep 2.0: humans now wake up rested. Known issue: Mondays
    still exist.
10. Fixed a bug where sleep required a dark room, a cold room, and an
    empty mind; sleep now ships with the mind included.

Verdict: candidate 1 wins. It is the most surprising (the fix is an
absurdly literal removal of the ceiling), the tersest, and it trusts
the reader instead of explaining the joke. Candidate 2 is the
runner-up: relatable, but its kicker ("like a normal job") explains
itself a little more. The rest are either wordy (3, 10), reuse the
3 a.m. replay idea already common in the field (4), or land as a
smile rather than a laugh (5, 6, 7, 8, 9).
"""

import os

# The winning patch note: one line, well under the 160-character cap.
LINE = (
    "Fixed a bug where falling asleep took 45 minutes of staring at "
    "the ceiling; the ceiling has been removed."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 160, f"line is {len(line)} chars, must be 1-160"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
