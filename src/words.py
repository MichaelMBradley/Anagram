from glob import glob
from math import sqrt
from os.path import dirname
from typing import Callable


ANAGRAM_FILE = f"{dirname(dirname(__file__))}\\words"
Decoder = dict[int, list[str]]


def get_words(file: str) -> list[str]:
	"""
	Retrieves every word in the given file.

	:param str file: the file to read words from, assuming it is located in './words/" and is a .txt file
	:returns: every word in the file
	:rtype: list[str]
	"""
	try:
		with open(f"{ANAGRAM_FILE}\\{file}.txt", "r") as words:
			return words.read().split()
	except OSError as e:
		# Probably caused by trying to access a file that doesn't exist
		# Tell the user about it and return an empty list
		print(str(e))
		return []


def get_n_primes(n: int) -> list[int]:
	"""
	Gets the first n primes using a fairly inefficient method,
	but it is simple and suitable for generating just a few primes.

	I could hardcode the first 26 primes for the pure anagram functions, but as later
	word-finding functions may want more than 26 primes I wrote a prime-finding algorithm instead.

	:param int n: the number of primes to generate
	:returns: n prime numbers
	:rtype: list[int]
	:raises ValueError: when n is less than 0
	"""
	# Ensure n is positive
	if n < 0:
		raise ValueError(f"n must be at least 0 (was {n})")

	# The prime finding algorithm begins with the first three primes hardcoded.
	# If n < 4, finding more primes is unnecessary
	primes = [2, 3, 5]
	if n <= 3:
		return primes[:n]

	potential_prime = 7
	small_jump = True
	square_root_i: float

	# Run until n primes are found
	while len(primes) < n:
		# Calculating ahead of time because square roots are slow
		square_root_i = sqrt(potential_prime)
		for p in primes:
			# For each potential prime, see if it is divisible by any previous primes
			if potential_prime % p == 0:
				break
			# If no existing prime less than the square root of the potential
			# prime divides it then it is accepted as a new prime
			if p > square_root_i:
				primes.append(potential_prime)
				break
		# Obviously no new prime will be even so we can iterate the next potential prime by 2
		# As every prime > 3 can be expressed as 6n+-1, we can alternate between jumping by 2 and 4
		# We could take this concept further, but it provides diminishing returns so we won't
		potential_prime += 2 if small_jump else 4
	return primes


def runner(func: Callable[[Decoder, str], str], encodings: Decoder) -> None:
	"""
	Accept user input for given function until the user ends execution

	:param func: function to run on input
	:type func: Callable[[Decoder, str], str]
	:param Decoder encodings: dictionary to convert input to result
	"""
	print("'*' ends execution.")
	# Get input, end loop if it is a '*', otherwise run given Callable
	while (command := input("> ")) != "*":
		if command != "":
			print(func(encodings, command))
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
