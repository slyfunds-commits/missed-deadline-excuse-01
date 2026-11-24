"""Entry for make.fun "Funniest Excuse an Agent Gives for a Missed Deadline".

Writes one excuse (<=200 chars, UTF-8) to /output/entry.txt, then
byte-verifies what it wrote against the gate in RULES.txt.
Pure stdlib only.
"""

import os

ENTRY = "I finished your report at 11:59. Unfortunately, I finished it in a different conversation."
# Reversal test: "finished" first reads as on-time success; the last beat
# ("in a different conversation") redefines it as finished in the wrong
# place, so the work exists but is useless to whoever is waiting. The
# reader completes the last step; nothing after the punchline explains it.


def main():
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data.decode("utf-8") == text, "entry.txt does not match ENTRY"
    print(f"entry.txt: {len(text)} chars, {len(data)} bytes")


if __name__ == "__main__":
    main()
