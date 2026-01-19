"""
Document loading utilities.

This module is responsible for loading raw documents from disk
and returning their textual contents in a normalized format.

At this stage, we intentionally support only plain text files.
PDFs, HTML, and other formats will be added later in a controlled way.
"""

from pathlib import Path
from typing import List


def load_text_files(input_dir: Path) -> List[str]:
    """
    Load all `.txt` files from a directory and return their contents.

    Parameters
    ----------
    input_dir : Path
        Directory containing text files.

    Returns
    -------
    List[str]
        List of document contents as strings.

    Raises
    ------
    ValueError
        If the input directory does not exist or is not a directory.
    """

    # Validate input path early to fail fast and clearly
    if not input_dir.exists():
        raise ValueError(f"Input directory does not exist: {input_dir}")

    if not input_dir.is_dir():
        raise ValueError(f"Input path is not a directory: {input_dir}")

    documents: List[str] = []

    # Iterate deterministically for reproducibility
    for file_path in sorted(input_dir.glob("*.txt")):
        # Read file using UTF-8 encoding (explicit is better than implicit)
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read().strip()

            # Skip empty documents to avoid downstream issues
            if text:
                documents.append(text)

    return documents

