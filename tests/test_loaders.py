"""
Tests for document loaders.

These tests validate that text files are correctly loaded
from disk and that invalid inputs are handled safely.
"""

from pathlib import Path
import pytest

from ingestion.loaders import load_text_files


def test_load_text_files_success(tmp_path: Path) -> None:
    """
    Load multiple text files from a directory.
    """

    # Create temporary text files
    file_1 = tmp_path / "doc1.txt"
    file_2 = tmp_path / "doc2.txt"

    file_1.write_text("First document", encoding="utf-8")
    file_2.write_text("Second document", encoding="utf-8")

    texts = load_text_files(tmp_path)

    assert len(texts) == 2
    assert "First document" in texts
    assert "Second document" in texts


def test_load_text_files_empty_directory(tmp_path: Path) -> None:
    """
    Loading from an empty directory should return an empty list.
    """

    texts = load_text_files(tmp_path)

    assert texts == []


def test_load_text_files_invalid_path() -> None:
    """
    Loading from a non-existing directory should raise an error.
    """

    with pytest.raises(ValueError):
        load_text_files(Path("non_existing_directory"))
