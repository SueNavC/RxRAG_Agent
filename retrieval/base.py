"""
Base definitions for retrieval components.

This module defines the abstract interface that any retriever
implementation must follow (FAISS, Pinecone, in-memory, etc.).

The goal is to decouple retrieval logic from its backend
and enforce a stable, testable contract.
"""

from abc import ABC, abstractmethod
from typing import List, Dict


class BaseRetriever(ABC):
    """
    Abstract base class for all retrievers.

    Any concrete retriever must implement the `retrieve` method
    and respect its input/output contract.
    """

    @abstractmethod
    def retrieve(self, query_embedding: List[float], top_k: int) -> List[Dict]:
        """
        Retrieve the most relevant chunks for a given query embedding.

        Parameters
        ----------
        query_embedding : List[float]
            Vector representation of the query.
        top_k : int
            Maximum number of results to return. Must be positive.

        Returns
        -------
        List[Dict]
            A list of retrieved items, each containing:
            - "text": str, the retrieved chunk text
            - "score": float, relevance score (higher is better)

        Raises
        ------
        ValueError
            If top_k is not a positive integer.
        """
        raise NotImplementedError
