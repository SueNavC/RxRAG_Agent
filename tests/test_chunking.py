"""
Unit tests for the text chunking logic.

These tests ensure that:
- Text is split deterministically
- Chunk sizes are respected
- Overlap is applied correctly
- Edge cases behave safely
"""

import pytest

from ingestion.chunking import chunk_text


def test_chunk_text_basic():
    """
    GIVEN a simple text
    WHEN chunking with a fixed size and no overlap
    THEN the text is split into equal-sized chunks
    """
    text = "abcdefghijklmnopqrstuvwxyz"  # 26 characters

    chunks = chunk_text(
        text=text,
        chunk_size=10,
        overlap=0,
    )

    assert chunks == [
        "abcdefghij",
        "klmnopqrst",
        "uvwxyz",
    ]


def test_chunk_text_with_overlap():
    """
    GIVEN a text
    WHEN chunking with overlap
    THEN consecutive chunks share overlapping characters
    """
    text = "abcdefghijABCDEFGHIJ"  # 20 characters

    chunks = chunk_text(
        text=text,
        chunk_size=10,
        overlap=3,
    )

    assert chunks == [
        "abcdefghij",
        "hijABCDEFG",
        "EFGHIJ",
    ]


def test_chunk_text_smaller_than_chunk():
    """
    GIVEN a text shorter than the chunk size
    WHEN chunking
    THEN the entire text is returned as a single chunk
    """
    text = "short text"

    chunks = chunk_text(
        text=text,
        chunk_size=100,
        overlap=10,
    )

    assert chunks == ["short text"]


def test_chunk_text_invalid_overlap():
    """
    GIVEN an invalid overlap (greater than or equal to chunk size)
    WHEN chunking
    THEN a ValueError is raised
    """
    with pytest.raises(ValueError):
        chunk_text(
            text="some text",
            chunk_size=10,
            overlap=10,
        )

