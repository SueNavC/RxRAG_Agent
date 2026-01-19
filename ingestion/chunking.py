"""
Text chunking utilities.

This module is responsible for splitting raw document texts into
smaller overlapping chunks that can later be embedded and indexed.

Chunking is intentionally implemented using character length rather
than tokens to keep this stage model-agnostic.
"""

from typing import List


def chunk_text(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200,
) -> List[str]:
    """
    Split a single text into overlapping chunks.

    Parameters
    ----------
    text : str
        Input document text.
    chunk_size : int
        Maximum size of each chunk (in characters).
    overlap : int
        Number of overlapping characters between consecutive chunks.

    Returns
    -------
    List[str]
        List of text chunks.

    Raises
    ------
    ValueError
        If chunk_size or overlap are invalid.
    """

    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks: List[str] = []

    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        # Move the window forward, keeping overlap
        start += chunk_size - overlap

    return chunks
