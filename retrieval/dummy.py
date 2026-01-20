"""
Dummy retriever implementation.

This module provides a minimal, deterministic retriever that
implements the BaseRetriever interface.

It is intended ONLY for:
- validating the retrieval contract
- supporting early development
- serving as a reference implementation

It does NOT perform real semantic search.
"""

from typing import List, Dict
from retrieval.base import BaseRetriever


class DummyRetriever(BaseRetriever):
    """
    A minimal retriever that returns fixed results.

    This implementation is backend-agnostic and deterministic.
    It exists to prove that the retrieval interface works as expected.
    """

    def retrieve(self, query_embedding: List[float], top_k: int) -> List[Dict]:
        """
        Return a fixed set of dummy retrieval results.

        Parameters
        ----------
        query_embedding : List[float]
            Vector representation of the query (ignored in this dummy).
        top_k : int
            Maximum number of results to return.

        Returns
        -------
        List[Dict]
            A list of retrieved chunks with text and score.
        """
        # Validate input explicitly to match the contract
        if top_k <= 0:
            raise ValueError("top_k must be a positive integer")

        # Fixed, deterministic dummy corpus
        results = [
            {"text": "Dummy chunk A", "score": 0.9},
            {"text": "Dummy chunk B", "score": 0.7},
            {"text": "Dummy chunk C", "score": 0.5},
        ]

        # Enforce top_k strictly
        return results[:top_k]
