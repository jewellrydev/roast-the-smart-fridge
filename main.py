#!/usr/bin/env python3
"""Smart, Allegedly — entry for Roast the Smart Fridge: One Line, Best Laugh Wins on make.fun.

Prints exactly one line (at most 160 characters) roasting a smart fridge.
"""

LINE = "The smart fridge ordered milk, judged my leftovers, and can keep neither a secret nor a cucumber fresh."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 160
    print(LINE)


if __name__ == "__main__":
    main()
