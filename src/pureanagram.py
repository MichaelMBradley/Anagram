from src.words import AnagramFinder, runner


class PureAnagram(AnagramFinder):
	"""
	Finds perfect anagrams of input words.
	"""
	encoded_words: dict[int: list[str]]

	def __init__(self, words_file: str) -> None:
		"""
		:param str words_file: the file to read valid words from
		"""
		self.encoded_words = {}
		super().__init__(words_file, 26)

	def add_word(self, word: str) -> None:
		"""
		Adds word to dictionary of valid words.

		:raises ValueError: if a character not in [a, z] | [A, Z] is in the input string
		"""
		encoding = self.encode_word(word)

		if encoding in self.encoded_words.keys():
			self.encoded_words[encoding].append(word)
		else:
			self.encoded_words[encoding] = [word]

	def get_anagrams(self, word: str) -> list[str]:
		encoding = self.encode_word(word)

		if encoding not in self.encoded_words.keys() or self.encoded_words[encoding] == [word]:
			raise ValueError(f"{word} -> no anagrams found.")

		return self.encoded_words[encoding]


if __name__ == "__main__":
	runner(PureAnagram("words_alpha"))
