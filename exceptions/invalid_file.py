"""InvalidFile.
This exception will be raised if given file is not ingestible.
"""


class InvalidFile(Exception):
    def __init__(
        self, ext, message="Invalid file! Please, provide a valid file!"
    ):
        self.message = f"Invalid file! Please, provide a valid {ext} file!"
        super().__init__(self.message)
