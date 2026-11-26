"""Make the AI Judge Laugh — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The joke: the standup meeting has spawned its own standup meeting, and even the Wi-Fi router refuses to sit through it.
TEXT = "Our standup meeting has a standup meeting now, and the only thing standing is the Wi-Fi router, because even it refuses to sit through this."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
