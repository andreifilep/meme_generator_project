"""Import quotes from known file types."""

from typing import List
import os
import subprocess

from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface


class PDFImporter(IngestorInterface):
    """Imports quotes from pdf files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of quotes from parsing pdf files using XpdfReader."""
        if not cls.can_ingest(path):
            raise ValueError(f'File type not supported for {path}')

        tmp = './temp.txt'
        call = subprocess.call(
            ['pdftotext', '-layout', path, tmp],
            shell=True,
            stderr=subprocess.STDOUT
        )

        quotes = []
        file_temp = open(tmp, "r")

        for line in file_temp.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                new_quote = QuoteModel(
                    line.split('-')[0].replace('"', ''),
                    line.split('-')[1])
                quotes.append(new_quote)

        file_temp.close()
        os.remove(tmp)
        return quotes
