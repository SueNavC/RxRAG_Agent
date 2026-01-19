from pathlib import Path
from typing import List


def load_text_files(input_dir: Path) -> List[str]:
    """
    Load all .txt files from a directory and return their contents as strings.
    """
    texts: List[str] = []

    for path in input_dir.glob("*.txt"):
        with open(path, "r", encoding="utf-8") as f:
            texts.append(f.read())

    return texts
