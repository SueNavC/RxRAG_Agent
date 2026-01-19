"""
Ingestion pipeline.

This module defines a simple, explicit pipeline that:
1. Loads raw documents from disk
2. Splits them into overlapping chunks

The output of this pipeline is a flat list of text chunks,
ready for downstream embedding and indexing.
"""

from pathlib import Path
from typing import List

from ingestion.loaders import load_text_files
from ingestion.chunking import chunk_text


def run_ingestion_pipeline(
    input_dir: Path,
    chunk_size: int = 1000,
    overlap: int = 200,
) -> List[str]:
    """
    Run the full ingestion pipeline: load documents and chunk them.

    Parameters
    ----------
    input_dir : Path
        Directory containing raw text documents.
    chunk_size : int
        Maximum size of each chunk (in characters).
    overlap : int
        Number of overlapping characters between chunks.

    Returns
    -------
    List[str]
        List of text chunks produced from all input documents.
    """

    # Step 1: Load raw documents
    documents = load_text_files(input_dir)

    # Step 2: Chunk each document and flatten the result
    all_chunks: List[str] = []

    for document in documents:
        chunks = chunk_text(
            text=document,
            chunk_size=chunk_size,
            overlap=overlap,
        )
        all_chunks.extend(chunks)

    return all_chunks
