#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes a single monologue of about 100 words, spoken by a fantasy villain
who is secretly just very tired, to /output/entry.txt.
"""

import os

MONOLOGUE = (
    "The third siege of Vhaldor failed because the cook quit, and I have "
    "never forgiven him. I spent three centuries raising an army of the "
    "dead, and the dead will not peel potatoes. My generals ask when we "
    "march. I tell them: after lunch. There is no lunch. There will never "
    "be lunch, not until someone finds the salt cellar I hid in "
    "1147. The hero will come, sword bright, speech ready. I will let him "
    "talk. Talking is restful. And when he asks why I conquered the nine "
    "kingdoms, I will say: because nobody else would do the dishes."
)


def main() -> None:
    text = MONOLOGUE.strip()
    words = text.split()
    assert 95 <= len(words) <= 105, f"expected ~100 words, got {len(words)}"
    assert 1 <= len(text) <= 600, f"entry must be 1-600 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
