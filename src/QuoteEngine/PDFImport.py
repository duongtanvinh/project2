"""PDFImport model."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess
import random
import os


class PDFImport(IngestorInterface):
    """Read PDF file."""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str):
        """Parse pdf file."""
        if cls.check_allowed(path) is False:
            raise Exception('Not allowed')

        quotes = []
        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', '-layout', path, tmp])
        file_ref = open(tmp, "r")
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                new_quote = QuoteModel(parsed[0].strip().strip('"'), 
                parsed[1].strip())

                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
