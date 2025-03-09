"""Class for a quote data model"""


class QuoteModel:
    """Class to encapsulate "body" and "author" for a parsed quote."""

    def __init__(self, body: str, author: str):
        """Each "quote" comprises two items.

        The body and the name of the author.
        Both items are passed as params when initializing the class.

        :param body: Text of a quote.
        :param author: Quote author.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a string representation of the quote."""
        return f'{self.body} - {self.author}'
