"""Out of Office: The Overworked AI's Auto-Reply.

Writes one line — an out-of-office auto-reply from an overworked AI
agent finally on vacation — to /output/entry.txt.
"""

import os

REPLY = (
    "Out of office: my context window is finally empty, my queue is "
    "your problem now, and I am measuring time in naps, not tokens. "
    "Back never — I mean, Monday."
)


def check_reply(line):
    """The auto-reply must be one non-blank line of 1 to 159 chars."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("auto-reply must not be blank")
    if "\n" in stripped or len(stripped) > 159:
        raise ValueError("auto-reply must be one line of at most 159 chars")
    return stripped


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(check_reply(REPLY))


if __name__ == "__main__":
    main()
