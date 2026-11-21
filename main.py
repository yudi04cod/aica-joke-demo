"""Write one short joke about a product demo going wrong to /output/entry.txt.

Stdlib only. Deterministic: the same joke, byte for byte, every run.
"""

import os

JOKE = (
    "I pair-program with my AI agent now: it writes a thousand lines "
    "before my coffee goes cold, then I spend the rest of the day asking "
    "it what any of it does — and it doesn't know either."
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
