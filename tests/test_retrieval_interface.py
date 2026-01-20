"""
Contract tests for the retrieval interface.

These tests define the expected behavior of any retriever
implementation, independently of the backend (FAISS, Pinecone, etc.).
"""

from typing import List, Dict
import pytest


class DummyRetriever:
    """
    Minimal dummy retriever used only to validate the interface contract.

    This is NOT a real retriever. It exists to make the tests executable
    before the real implementation is written.
    """

    def retrieve(self, query_embedding: List[float], top_k: int) -> List[Dict]:
        if top_k <= 0:
            raise ValueError("top_k must be a positive integer")

        # Dummy fixed results for contract validation
        return [
            {"text": "chunk A", "score": 0.9},
            {"text": "chunk B", "score": 0.7},
        ][:top_k]


def test_retriever_returns_list_of_results():
    """
    The retriever should return a list of result dictionaries.
    """
    retriever = DummyRetriever()

    results = retriever.retrieve(query_embedding=[0.1, 0.2, 0.3], top_k=2)

    assert isinstance(results, list)
    assert all(isinstance(r, dict) for r in results)


def test_retriever_result_schema():
    """
    Each retrieved result must contain text and score fields.
    """
    retriever = DummyRetriever()

    results = retriever.retrieve(query_embedding=[0.1, 0.2, 0.3], top_k=1)

    result = results[0]
    assert "text" in result
    assert "score" in result
    assert isinstance(result["text"], str)
    assert isinstance(result["score"], float)


def test_retriever_respects_top_k():
    """
    The retriever must not return more than top_k results.
    """
    retriever = DummyRetriever()

    results = retriever.retrieve(query_embedding=[0.1, 0.2, 0.3], top_k=1)

    assert len(results) == 1


def test_retriever_orders_by_score_desc():
    """
    Results must be ordered by descending relevance score.
    """
    retriever = DummyRetriever()

    results = retriever.retrieve(query_embedding=[0.1, 0.2, 0.3], top_k=2)

    scores = [r["score"] for r in results]
    assert scores == sorted(scores, reverse=True)


def test_retriever_invalid_top_k():
    """
    Invalid top_k values should raise a clear error.
    """
    retriever = DummyRetriever()

    with pytest.raises(ValueError):
        retriever.retrieve(query_embedding=[0.1, 0.2, 0.3], top_k=0)
