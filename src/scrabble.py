from words import runner, AnagramFinder


class ScrabbleWordFinder(AnagramFinder):
	def __init__(self, words_file: str):
		super().__init__(words_file, 0)

	def add_word(self, word: str):
		pass

	def encode_word(self, word: str) -> int:
		pass

	def get_anagrams(self, word: str) -> list[str]:
		pass


if __name__ == "__main__":
	runner(ScrabbleWordFinder("words_alpha"))
