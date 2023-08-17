"""Quote Model."""


class QuoteModel:
    """Quote Model."""

    def __init__(self, body, author):
        """Create a new QuoTeModel."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return str."""
        return f"{self.body} - {self.author}"
