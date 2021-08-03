from primes import get_n_primes
from words import get_all, InvalidCharacterException, NoAnagramsException

primes = get_n_primes(26)


def encode_word(string: str) -> int:
	"""
	Encodes a string into an integer equalling the product of the prime associated with each letter in the string.

	Parameters
	----------
	string: str
		The string to be encoded.

	Returns
	-------
	int
		The product of the prime associated with each letter ({'a': 2, 'b': 3, 'c': 5, ...}).

	Raises
	------
	InvalidCharacterException
		Raised if a character not in (a-z) or (A-Z) is in the input string.
	"""
	product = 1
	for char in string:
		ind = ord(char.lower()) - ord('a')
		if 0 <= ind <= 26:
			product *= primes[ind]
		else:
			raise InvalidCharacterException(char, string)
	return product


def encode_words_file(file: str = "words_alpha") -> dict[int: list[str]]:
	"""
	Encodes all of the words in a given file.

	Parameters
	----------
	file: str, optional
		The file to encode.

	Returns
	-------
	dict[int: list[str]]
		Each list contains only strings whose encodings are equivalent to the key (they're anagrams of each other).
	"""
	encoded = {}
	for word in get_all(file):
		try:
			enc = encode_word(word)
			if enc in encoded.keys():
				encoded[enc].append(word)
			else:
				encoded[enc] = [word]
		except InvalidCharacterException as e:
			print(e)
	return encoded


def get_anagrams(encoded: dict[int: list[str]], word: str) -> list[str]:
	"""
	Finds all anagrams of a given string.

	Parameters
	----------
	encoded: dict[int: list[str]]
		The encoded set of valid words, provided by encode_words_file().
	word: str
		The string to check for anagrams.

	Returns
	-------
	list[str]
		The list of all anagrams of the input string.

	Raises
	------
	InvalidCharacterException
		Raised if a character not in (a-z) or (A-Z) is in the input string.
	NoAnagramsException
		Raised if there are no anagrams of the given word.
	"""
	try:
		enc = encode_word(word)
		if enc not in encoded.keys() or (anagrams := encoded[enc]) == [word.lower()]:
			raise NoAnagramsException(word)
		return anagrams
	except InvalidCharacterException as e:
		raise e


def anagrams_to_string(encoded: dict[int: str], word: str) -> str:
	"""
	Outputs anagrams from get_anagrams() in a more readable format, and handles exceptions.

	Parameters
	----------
	encoded: dict[int: list[str]]
		The encoded set of valid words, provided by encode_words_file().
	word: str
		The string to check for anagrams.

	Returns
	-------
	str
		The formatted output string.
	"""
	wordlist = ""
	try:
		for i, anagram in enumerate(get_anagrams(encoded, word)):
			if anagram != word.lower():
				wordlist += f"{anagram}, "
		return wordlist[0].upper() + wordlist[1:-2] + '.'
	except InvalidCharacterException as e:
		return f"{word} contains an invalid character, '{e.character}'."
	except NoAnagramsException as e:
		return str(e)


if __name__ == "__main__":
	encodings = encode_words_file()
	print("Enter a word to get its encoding.\n'*' ends execution.")
	while True:
		command = input("> ")
		if command == '*':
			break
		else:
			print(anagrams_to_string(encodings, command))
