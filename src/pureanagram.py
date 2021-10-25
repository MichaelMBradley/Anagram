from src.words import AnagramFinder, runner


class PureAnagram(AnagramFinder):
	encoded_words: dict[int: list[str]]

	def __init__(self, words_file: str) -> None:
		self.encoded_words = {}
		super().__init__(words_file, 26)

	def add_word(self, word: str) -> None:
		"""
		Adds

		:raises ValueError: if a character not in [a, z] | [A, Z] is in the input string
		"""
		try:
			product = self.encode_word(word)
		except ValueError as e:
			raise e

		if product in self.encoded_words.keys():
			self.encoded_words[product].append(word)
		else:
			self.encoded_words[product] = [word]

	def encode_word(self, word: str) -> int:
		"""
		Encodes a string into an integer equalling the product of the prime associated with each letter in the string.

		:param str word: word to be encoded
		:raises ValueError: if a character not in [a, z] | [A, Z] is in the input string
		"""
		product = 1

		for char in word:
			# Get index of character from a=0 to z=25
			ind = ord(char.lower()) - ord("a")
			if 0 <= ind < 26:
				product *= self.primes[ind]
			else:
				raise ValueError(f"{word} -> {char} is an invalid character.")

		return product

	def get_anagrams(self, word: str) -> list[str]:
		encoding: int

		try:
			encoding = self.encode_word(word)
		except ValueError as e:
			raise e

		if encoding not in self.encoded_words.keys() or self.encoded_words[encoding] == [word]:
			raise ValueError(f"{word} -> no anagrams found.")
		else:
			return self.encoded_words[encoding]


if __name__ == "__main__":
	runner(PureAnagram("words_alpha"))
