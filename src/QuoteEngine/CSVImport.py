"""CSVImport model."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas


class CSVImport(IngestorInterface):
    """Read CSV file."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str):
        """Parse CSV file."""
        if cls.check_allowed(path) is False:
            raise Exception('Not allowed')

        quotes = []
        df = pandas.read_csv(path, header=0)
        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        return quotes
