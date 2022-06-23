""" Quote Model """


class QuoteModel:
    """Quote Model.
    A model for building quotes."""

    def __init__(self, author, body):
        self.author = author
        self.body = body

    def __repl__(self) -> str:
        """Returns a human-readable quote with the author"""
        return f'"{self.body}" - {self.author}'

    def __str__(self) -> str:
        """Returns a human-readable quote with the author"""
        return self.__repl__()
