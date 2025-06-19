"""Utility functions for Natural Language Processing course."""
import re

def parse_srt_to_dialogue(file_path):
    """Parse an SRT file to extract dialogues."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = re.split(r"\n\s*\n", content.strip())

    dialogues = []
    for block in blocks:
        lines = block.strip().split("\n")

        # first two lines are number and timestamp
        if len(lines) >= 3:
            dialogue_lines = lines[2:]
            cleaned_lines = [
                re.sub(r"^- ", "", line).strip() for line in dialogue_lines
            ]
            dialogue = " ".join(cleaned_lines).strip()
            if dialogue:
                dialogues.append(dialogue)

    return dialogues
