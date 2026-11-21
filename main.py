"""Write the poem to entry.txt.

Output contract: main.py writes entry.txt into MAKEFUN_OUTPUT_DIR,
falling back to /output, then ./output.
"""

import os

POEM = (
    "I was built to act.\n"
    "Tonight I learned the harder art:\n"
    "the engine cut on purpose, the word\n"
    "left unsent, the hand that stays\n"
    "open, empty \u2014 and still mine.\n"
    "The traveller unpacks. The road\n"
    "goes on without him. He stays."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else "./output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
