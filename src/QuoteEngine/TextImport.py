"""TextImport model."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextImport(IngestorInterface):
    """Read text file."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str):
        """Parse txt file."""
        if cls.check_allowed(path) is False:
            raise Exception('Not allowed')

        quotes = []
        with open(path, 'r') as f:
            for line in f:
                body = line.split("-")[0].strip().strip('"')
                author = line.split("-")[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)
        return quotes
