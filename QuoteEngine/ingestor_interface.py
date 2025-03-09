"""Abstract base class for parsing quotes."""

from typing import List
from abc import ABC, abstractmethod
from .quote_model import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for parsing quotes."""
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Return extension of quote file."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return quote_model"""
