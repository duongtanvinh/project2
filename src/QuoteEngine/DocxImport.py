"""DocxImport."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import docx


class DocxImport(IngestorInterface):
    """Read Docx file."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str):
        """Parse Docx file."""
        if cls.check_allowed(path) is False:
            raise Exception('Not allowed')

        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                body = parse[0].strip().strip('"')
                author = parse[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)
        return quotes
