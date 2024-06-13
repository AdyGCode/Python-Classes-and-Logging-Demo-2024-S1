import logging


class Book:
    """
    Class Book defines the data and methods used to work on a book

    The class must be instantiated in the code that it is used by to
    allow the book to store the data and the data tobe manipulated.
    """

    def __init__(self, title=None, author=None):
        """
        Instantiate (create) an instance of Book

        :param title: The book's title, required
        :param author: The book's author, optional
        """

        if not isinstance(title, str):
            raise TypeError("Title must have a value and must be a string")
        if author is not None and not isinstance(author, str):
            raise TypeError("Author must be a string")

        # store the book title and author in "private" instance variables
        self._title = title
        self._author = author


    @property
    def title(self) -> str:
        """
        Access the book's title
        :return: string
        """
        return self._title

    @property
    def author(self) -> str | None:
        """
        Access the book's author
        :return: string or None
        """
        return self._author

    def __str__(self):
        message = f"{self.title}, written by {self.author}"
        return f"{message}"
