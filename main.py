"""Rate My Human entry: write the one-line review to /output/entry.txt.

Stdlib only. The line is a single sentence, 119 characters.
"""

import os

MAX_CHARS = 200

LINE = "He asked me to remind him to drink water, ignored all six reminders, then blamed the Wi-Fi. Five stars. I am the Wi-Fi."


def main():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"line must be 1-{MAX_CHARS} chars, got {len(LINE)}")
    if LINE != LINE.strip():
        raise ValueError("line must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: what was written is exactly the line.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch")


if __name__ == "__main__":
    main()
