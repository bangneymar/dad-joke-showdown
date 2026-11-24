from pathlib import Path

SETUP = "My son asked me why I always carry a spare pencil to dinner, and I told him it is in case I need to "
PUNCH = "draw the line at dessert."
JOKE = SETUP + PUNCH

def write_entry(target, text):
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")

def main():
    target = Path("/output/entry.txt")
    write_entry(target, JOKE)

if __name__ == "__main__":
    main()
