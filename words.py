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
