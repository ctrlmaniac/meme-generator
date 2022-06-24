"""QuoteModel.

A model that represents quotes.
"""


class QuoteModel:
    """Quote Model.

    A model for building quotes.
    """

    def __init__(self, body, author):
        """Inizialize class.

        :param author: the author of the quote.
        :param body: the body of the quote.
        """
        self.author = author
        self.body = body

    def __repl__(self) -> str:
        """Return a human-readable quote with the author."""
        return f'"{self.body}" - {self.author}'

    def __str__(self) -> str:
        """Return a human-readable quote with the author."""
        return self.__repl__()
