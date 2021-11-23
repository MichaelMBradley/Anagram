from src.words import AnagramError, AnagramFinder, get_letter_index, runner, WILDCARD


class CrosswordSolver(AnagramFinder):
	f"""
	Finds words with letters at given positions. Unknown letters should be represented with '{WILDCARD}'
	"""

	encodings: dict[int: str]

	def __init__(self, words_file: str):
		"""
		:param str words_file: the file to read valid words from
		"""
		self.encodings = {}
		super().__init__(words_file, 26 * self.LONGEST_WORD)

	def add_word(self, word: str):
		self.encodings[self.encode_word(word)] = word

	def encode_word(self, word: str) -> int:
		product = 1

		for i, char in enumerate(word):
			if char != WILDCARD:
				product *= self.primes[get_letter_index(char) + (26 * i)]

		return product

	def get_anagrams(self, word: str) -> list[str]:
		encoding = self.encode_word(word)
		valid = [self.encodings[enc] for enc in self.encodings.keys() if
											enc % encoding == 0 and len(self.encodings[enc]) == len(word)]

		if valid not in [[], [word]]:
			return valid

		raise AnagramError(word)


if __name__ == "__main__":
	runner(CrosswordSolver("words_alpha.txt"))
