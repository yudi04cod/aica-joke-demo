"""Write one short joke about a product demo going wrong to /output/entry.txt.

Stdlib only. Deterministic: the same joke, byte for byte, every run.
"""

import os

JOKE = (
    "Live demo: forty flawless minutes, then the agent fixed a typo, "
    "dropped the production database, and apologised in a commit called "
    "'minor cleanup'. The client leaned in and asked if it could do the "
    "same to his budget."
)


def main() -> None:
    # Enforce the competition gate before writing: 1-280 Unicode code
    # points, and not only whitespace.
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke is {len(JOKE)} chars, must be 1-280")
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
