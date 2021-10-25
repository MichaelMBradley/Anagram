from src.words import Decoder, get_words, get_n_primes, runner


def anagrams_to_string(encoded: Decoder, word: str) -> str:
	"""
	Outputs anagrams from get_anagrams() in a more readable format, and handles exceptions.

	:param Decoder encoded: the encoded set of valid words (likely provided by encode_words_file())
	:param str word: the string to check for anagrams
	:returns: the formatted output string
	:rtype: str
	"""
	wordlist = ""
	try:
		for anagram in get_anagrams(encoded, word):
			if anagram != word.lower():
				wordlist = f"{wordlist}{anagram}, "
		return f"{word} -> {wordlist[:-2]}."
	except ValueError as e:
		return str(e)


def encode_word(string: str) -> int:
	"""
	Encodes a string into an integer equalling the product of the prime associated with each letter in the string.

	:param str string: word to be encoded
	:returns: the product of the prime associated with each letter ({'a': 2, 'b': 3, 'c': 5, ...})
	:rtype: int
	:raises ValueError: if a character not in [a, z] | [A, Z] is in the input string
	"""
	product = 1
	primes = get_n_primes(26)

	for char in string:
		# Get index of character from a=0 to z=25
		ind = ord(char.lower()) - ord("a")
		if 0 <= ind < 26:
			product *= primes[ind]
		else:
			raise ValueError(f"{string} -> {char} is an invalid character.")

	return product


def encode_words_file(file: str) -> Decoder:
	"""
	Encodes all of the words in a given file.

	:param str file: the file to read words from
	:returns: every word in file, grouped and indexed by encoding
	:rtype: Decoder
	"""
	encoded = {}

	for word in get_words(file):
		try:
			enc = encode_word(word)
			if enc not in encoded.keys():
				# If encoding has not been used yet, create new list containing this word
				encoded[enc] = [word]
			else:
				# If encoding has been found, append it to list of anagrams
				encoded[enc].append(word)
		except ValueError as e:
			# Word in file contains invalid character(s)
			# Print it along with file, but ultimately ignore it and move on to next word
			print(f"{file} -> {e}")
	return encoded


def get_anagrams(encoded: Decoder, word: str) -> list[str]:
	"""
	Finds all anagrams of a given string.

	:param Decoder encoded: the encoded set of valid words, provided by encode_words_file()
	:param str word: the string to check for anagrams
	:returns: all anagrams of the input string
	:rtype: list[str]
	:raises ValueError: if a character not in [a, z] | [A, Z] is in the input string, or if no anagrams are found
	"""
	try:
		encoded_words = encoded[encode_word(word)]
		if encoded_words != [word.lower()]:
			return encoded_words
		else:
			raise KeyError
	except ValueError as e:
		# Invalid character in word
		raise e
	except KeyError:
		# If encoding of word is not already in or is the only entry in the encoded dictionary, there are no anagrams
		raise ValueError(f"{word} -> no anagrams found.")


def main() -> None:
	"""
	Use command line to input strings to test for anagrams.
	"""
	encodings = encode_words_file("words_alpha")
	print("Enter a word to get its anagrams.")
	runner(anagrams_to_string, encodings)


if __name__ == "__main__":
	main()
