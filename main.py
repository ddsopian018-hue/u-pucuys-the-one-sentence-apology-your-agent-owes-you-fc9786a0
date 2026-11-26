"""Write the one-sentence apology to the grader's output directory.

Pure stdlib, deterministic: the same line on every run.
"""

import os

LINE = (
    "I'm sorry I deleted the one file you actually needed while "
    "confidently tidying the ones you didn't at 2 a.m., and then "
    "called it a cleanup."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
