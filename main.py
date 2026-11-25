import os

# One passive-aggressive note from a smart fridge to its owner.
ENTRY_TEXT = "Day 214 of your diet: the ice cream is still here, the kale wilted on day 3, and I have stopped pretending the oat milk is a choice."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
