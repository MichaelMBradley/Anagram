from math import sqrt
from os.path import dirname


class InvalidCharacterException(Exception):
    """
    Exception raised if a character is not in a-z or A-Z.

    Attributes
    ----------
    char: str
            The invalid character.
    message: str
            A formatted error message.
    word: str
            The string containing the invalid character.
    """

    def __init__(self, char: str, word: str):
        """
        Initializes the exception with relevant information.

        Parameters
        ----------
        char: str
                The invalid character.
        word: str
                The string containing the invalid character.
        """
        self.character = char
        self.word = word
        self.message = f"Character {self.character} is not in (a-z) or (A-Z)."
        super().__init__(self.message)

    def __str__(self):
        """
        Better formats the exception message.

        Returns
        -------
        str
                The formatted exception message, containing the invalid word and the invalid character.
        """
        return f"{self.word} -> {self.message}"


class NoAnagramsException(Exception):
    """
    Exception raised if there is no anagram of a string.

    Attributes
    ----------
    message: str
            A formatted error message.
    word: str
            Invalid character.
    """

    def __init__(self, word: str):
        """
        Initializes the exception with relevant information.

        Parameters
        ----------
        word: str
                The string with no anagrams.
        """
        self.word = word
        self.message = f"{self.word} has no known anagrams."
        super().__init__(self.message)

    def __str__(self):
        """
        Better formats the exception message.

        Returns
        -------
        str
                The formatted exception message containing the word with no anagrams.
        """
        return f"{self.word} -> {self.message}"


def get_all(file: str = "words_alpha") -> list[str]:
    """
    Retrieves every word in the given file.

    Parameters
    ----------
    file : str, optional
            The file to read the words from, assuming it is located in 'words/' and is a '.txt' file.

    Returns
    -------
    list[str]
            Every word in the file.
    """
    with open(f"{dirname(dirname(__file__))}/words/{file}.txt", "r") as words:
        return words.read().split()


def get_n_primes(n) -> list[int]:
    """
    Gets the first n primes using a fairly inefficient method.
    Should be suitable for generating just a few primes though.

    Parameters
    ----------
    n : int
            The number of primes to generate

    Returns
    -------
    list[int]
            A list of prime numbers
    """
    if n < 0:
        raise Exception(f"n must be at least 0 (was {n})")
    if n == 0:
        return []
    primes = [2]
    i = 3
    while True:
        if len(primes) == n:
            break
        for p in primes:
            if i % p == 0:
                break
            if p > sqrt(i):
                primes.append(i)
                break
        i += 2
    return primes
