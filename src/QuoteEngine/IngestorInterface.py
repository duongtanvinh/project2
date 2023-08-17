"""Ingestor Interface."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class."""
    allowed_extensions = []

    @classmethod
    def check_allowed(cls, path) -> bool:
        """Check extension file."""
        exten = path.split('.')[-1]
        if exten in cls.allowed_extensions:
            return True
        return False

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstractmethod."""
        pass
