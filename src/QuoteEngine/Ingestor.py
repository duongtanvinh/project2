"""Ingestor Model."""

from .IngestorInterface import IngestorInterface
from .CSVImport import CSVImport
from .DocxImport import DocxImport
from .PDFImport import PDFImport
from .TextImport import TextImport
from QuoteEngine.QuoteModel import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    """Class Ingestor."""

    ingestors = [CSVImport, DocxImport, PDFImport, TextImport]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Path file."""
        for ingestor in cls.ingestors:
            if ingestor.check_allowed(path) is True:
                return ingestor.parse(path)
