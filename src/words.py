from abc import ABC, abstractmethod
from glob import glob
from math import sqrt
from os.path import dirname


ANAGRAM_FILE = f"{dirname(dirname(__file__))}\\words"


class AnagramFinder(ABC):
	"""
	Provides a base class to streamline implementation of word-finding algorithms.

	A subclass must implement the add_word() and get_anagrams() methods.
	"""
	LONGEST_WORD = 32
	primes: list[int]

	def __init__(self, words_file: str, n_primes: int) -> None:
		"""
		Initialize primes, then encode all words in the given file.

		:param str words_file: the file to read valid words from
		:param int n_primes: the number of primes to generate
		"""
		# The goal of this project is to mes around with using primes to find anagrams,
		# so n primes must always be generated
		self.get_n_primes(n_primes)
		# Encodes the words in the given file using abstract methods
		self.encode_words_file(words_file)
		# Once this code is run, a properly implemented subclass will be able to find anagrams immediately

	@abstractmethod
	def add_word(self, word: str) -> None:
		"""
		Save word to valid word list with whatever encodings and computations are necessary.

		:param str word: the word to save
		"""
		pass

	def anagrams_to_string(self, word: str) -> str:
		"""
		Finds relevant anagrams of input string.

		:param str word: the string to check for anagrams
		:returns: the formatted output string
		:rtype: str
		"""
		wordlist = ""
		try:
			for anagram in self.get_anagrams(word):
				# Don't include input word in output
				if anagram != word.lower():
					wordlist = f"{wordlist}{anagram}, "
			# Format, replace final ', ' with '.'
			return f"{word} -> {wordlist[:-2]}."
		except ValueError as e:
			# Invalid character in word
			return str(e)

	def encode_word(self, word: str) -> int:
		"""
		Encodes a string into an integer equalling the product of the prime associated with each letter in the string.

		:param str word: word to be encoded
		:returns: encoding of word
		:rtype: int
		:raises ValueError: if a character not in [a, z] | [A, Z] is in the input string, or if the word is too long
		"""
		if len(word) >= self.LONGEST_WORD:
			raise ValueError(f"{word[:3]}... -> word is too long! (length >= {self.LONGEST_WORD}).")

		product = 1
		for char in word:
			product *= self.primes[get_letter_index(char)]

		return product

	def encode_words_file(self, file: str) -> None:
		"""
		Encodes all of the words in a given file.

		:param str file: the file to read words from
		"""
		try:
			with open(f"{ANAGRAM_FILE}\\{file}.txt", "r") as words:
				for word in words.read().split():
					try:
						self.add_word(word)
					except ValueError as e:
						# If any words in the file contain invalid characters
						print(str(e))
		except OSError as e:
			# Probably caused by trying to access a file that doesn't exist
			# Tell the user about it and return an empty list
			print(str(e))

	@abstractmethod
	def get_anagrams(self, word: str) -> list[str]:
		"""
		Finds valid anagrams by whatever method is relevant.

		:param word: word to find anagrams of
		:return: list of valid anagrams
		:rtype: list[str]
		"""
		pass

	def get_n_primes(self, n: int) -> None:
		"""
		Gets the first n primes using a fairly inefficient method,
		but it is simple and suitable for generating just a few primes.

		I could hardcode the first 26 primes for the pure anagram functions, but as other
		word-finding functions may want more than 26 primes I wrote a prime-finding algorithm instead.

		:param int n: the number of primes to generate
		:raises ValueError: when n is less than 0
		"""
		# Ensure n is positive
		if n < 0:
			raise ValueError(f"n must be at least 0 (was {n})")

		# The prime finding algorithm begins with the first three primes hardcoded.
		# If n < 4, finding more primes is unnecessary
		found_primes = [2, 3, 5]
		if n <= 3:
			self.primes = found_primes[:n]
			return

		potential_prime = 7
		small_jump = True
		square_root_i: float

		# Run until n primes are found
		while len(found_primes) < n:
			# Calculating ahead of time because square roots are slow
			square_root_i = sqrt(potential_prime)
			for p in found_primes:
				# For each potential prime, see if it is divisible by any previous primes
				if potential_prime % p == 0:
					break
				# If no existing prime less than the square root of the potential
				# prime divides it then it is accepted as a new prime
				if p > square_root_i:
					found_primes.append(potential_prime)
					break
			# Obviously no new prime will be even so we can iterate the next potential prime by 2
			# As every prime > 3 can be expressed as 6n+-1, we can alternate between jumping by 2 and 4
			# I could take this concept further, but it provides diminishing returns so I won't
			potential_prime += 2 if small_jump else 4

		self.primes = found_primes


def get_letter_index(char: str) -> int:
	"""
	Returns the position of a letter in the alphabet, where a=0 and z=25

	:param str char: character to index
	:return: index of character
	:rtype: int
	"""
	if len(char) != 1:
		raise ValueError(f"{char} -> does not have length 1.")
	else:
		# Make character lowercase, offset by ASCII of 'a'
		ind = ord(char.lower()) - ord("a")
		if 0 <= ind < 26:
			return ind
		else:
			raise ValueError(f"{char} -> not in [a, z] | [A, Z].")


def runner(anagram_finder: AnagramFinder) -> None:
	"""
	Accept user input for given function until the user ends execution

	:param AnagramFinder anagram_finder: object to find anagrams of input with
	"""
	print("'*' ends execution.")
	# Get input, end loop if it is a '*', otherwise find anagrams using given object
	while (command := input("> ")) != "*":
		if command != "":
			print(anagram_finder.anagrams_to_string(command))
		else:
			print("Please enter a string.")


def word_intersection() -> None:
	"""
	Runs through every text file in ./words/ and creates a new file
	(intersect.txt) that contains only the words that are in each file
	"""
	wordlists: list[set[str]] = []
	for file in glob(f"{ANAGRAM_FILE}\\*"):
		if file.split("\\")[-1] == "intersect.txt":
			# Avoid reading previously generated intersection file
			continue
		with open(file, "r") as wordlist:
			wordlists.append(set(wordlist.read().split()))

	# Intersect wordlists[0] with all other wordlists to get intersection of all wordlists
	for wordlist in wordlists[0:]:
		wordlists[0] = wordlists[0].intersection(wordlist)

	# Write intersection to file
	with open(f"{ANAGRAM_FILE}\\intersect.txt", "w") as best:
		for i, word in enumerate(wordlists[0]):
			best.write(word)
			# Create a new line if the word is not the last
			if i != len(wordlists[0]) - 1:
				best.write("\n")


if __name__ == "__main__":
	word_intersection()
