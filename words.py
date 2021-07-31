class InvalidCharacterException(Exception):
    """
    Exception raised if character is not in a-z or A-Z.

    Attributes:
    char: str
        Invalid character
    """
    def __init__(self, char: str):
        self.character = char
        self.message = f"Character {self.character} is not in (a-z) or (A-Z)"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.character} -> {self.message}"


def get_all(file: str = "words_alpha") -> list[str]:
    """
    Retrieves every word in the given file.

    Parameters
    ----------
    file : str (optional)
        The file to read the words from, assuming it is located in 'words/' and is a '.txt' file.

    Returns
    -------
    list[str]
        Every word in the file.
    """
    with open(f"words/{file}.txt") as words:
        return words.read().split()


if __name__ == "__main__":
    print(get_all())
