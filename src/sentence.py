from src.words import runner
from src.scrabble import ScrabbleWordFinder


class SentenceFinder(ScrabbleWordFinder):
	"""
	Effectively runs the scrabble word finder recursively on the letters not used from the input in each valid word.
	"""
	def get_anagrams(self, word: str) -> list[str]:
		pass


if __name__ == "__main__":
	runner(SentenceFinder("words_alpha"))
