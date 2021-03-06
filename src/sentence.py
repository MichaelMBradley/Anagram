from src.words import AnagramError, runner, WILDCARD
from src.scrabble import ScrabbleWordFinder


class SentenceFinder(ScrabbleWordFinder):
	"""
	Runs the Scrabble word finder recursively on the letters not used from the input in each valid word.

	Slow as hell on large inputs.
	"""

	def get_anagrams(self, word: str) -> list[str]:
		try:
			encoded_word = self.encode_word("".join(filter(lambda c: c != WILDCARD, word)))
			# FIXME: This is nigh-unreadable
			return self.get_anagrams_by_attributes(
				encoded_word,
				len(word),
				[
					{k: v for (k, v) in word_len.items() if max(encoded_word, k) % min(k, encoded_word) == 0}
					for word_len in self.encoded
				])
		except ValueError as e:
			raise e

	# TODO: Optimize
	def get_anagrams_by_attributes(
			self,
			encoded_word: int,
			length_of_word: int,
			relevant_encodings: list[dict[int: list[str]]]
	) -> list[str]:
		"""
		Allows for easier recursion by just using properties of words, not the words themselves.

		:param int encoded_word: encoding of the word
		:param int length_of_word: length of the word
		:param relevant_encodings: the list of encoded words with any encodings that could not possibly be used removed
		:type relevant_encodings: list[dict[int: list[str]]]
		:returns: all sentences of words made by rearranging letters of the input
		:rtype: list[str]
		"""
		valid_words: list[str] = []

		# Iterate through every encoding of words with a length <= the input
		# Iterating from high to low word lengths subjectively creates a nicer output
		for word_length in range(length_of_word, 0, -1):
			for encoding in relevant_encodings[word_length].keys():
				# If the current encoding divides the input encoding, it can be made from the letters in the input
				# If wildcards are input then the current encoding may be greater than the input encoding,
				# but it will still be a valid sub-word (so we must max()/min())
				if max(encoded_word, encoding) % min(encoding, encoded_word) == 0:
					# For each word that can be made from the input
					for scrabble_word in relevant_encodings[word_length][encoding]:
						encoded_scrabble_word = self.encode_word(scrabble_word)
						# Dividing the input encoding by the scrabble word encoding effectively removes the
						# letters in the scrabble word from the input, allowing us to recursively call
						# get_anagrams_by_attributes() on the string of unused characters
						try:
							for fragment in self.get_anagrams_by_attributes(
									max(encoded_word, encoded_scrabble_word) // min(encoded_scrabble_word, encoded_word),
									length_of_word - len(scrabble_word),
									relevant_encodings):
								# Each fragment represents the best attempt to use the rest of the letters in the input
								valid_words.append(f"{scrabble_word} {fragment}")
						except ValueError:
							# If there are no anagrams, just return the last valid sub-word
							valid_words.append(scrabble_word)

		if len(valid_words) == 0:
			raise AnagramError(str(encoded_word))

		return valid_words


if __name__ == "__main__":
	runner(SentenceFinder("intersect.txt"))
