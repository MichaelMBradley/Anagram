from src.words import AnagramError, AnagramFinder, runner, WILDCARD


class ScrabbleWordFinder(AnagramFinder):
	f"""
	Finds all words that can be formed from the letters of the input string.
	Named ScrabbleWordFinder as it can be used for that purpose, but unlike Scrabble contains no length limit.

	Use {WILDCARD} as a wildcard.
	"""
	encoded: list[dict[int: list[str]]]

	def __init__(self, words_file: str):
		"""
		:param str words_file: the file to read valid words from
		"""
		self.encoded = []
		for _ in range(self.LONGEST_WORD):
			self.encoded.append({})
		super().__init__(words_file, 26)

	def add_word(self, word: str):
		"""
		Adds word to dictionary of valid words.

		:raises ValueError: if a character not in [a, z] | [A, Z] is in the input string
		"""
		encoding = self.encode_word(word)
		encoded_words = self.encoded[len(word)]

		# Map words to encodings, but grouped by word length
		if encoding in encoded_words.keys():
			encoded_words[encoding].append(word)
		else:
			encoded_words[encoding] = [word]

	def get_anagrams(self, word: str) -> list[str]:
		valid_words: list[str] = []
		encoded_word = self.encode_word("".join(filter(lambda c: c != WILDCARD, word)))

		for word_length in range(len(word), 0, -1):
			for encoding in self.encoded[word_length].keys():
				if max(encoded_word, encoding) % min(encoding, encoded_word) == 0:
					valid_words += self.encoded[word_length][encoding]

		if not valid_words:
			raise AnagramError(word)

		return valid_words


if __name__ == "__main__":
	runner(ScrabbleWordFinder("words_alpha.txt"))
