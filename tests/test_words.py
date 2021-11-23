import unittest
from unittest import TestCase

from src.words import ANAGRAM_FILE, AnagramFinder, word_intersection


# This class only exists to implement the abstract AnagramFinder class so that its built-in methods can be tested
# That being said, it can also be copy-pasted to provide a good starting point for a new anagram finder
class AnagramFinderTester(AnagramFinder):
	def __init__(self, words_file: str):
		super().__init__(words_file, 0)

	def add_word(self, word: str):
		pass

	def encode_word(self, word: str) -> int:
		pass

	def get_anagrams(self, word: str) -> list[str]:
		pass


af_tester = AnagramFinderTester("words_alpha.txt")


class TestWords(TestCase):
	def test_get_n_primes(self):
		self.assertIsInstance(af_tester.primes, list)
		# Testing prime generation
		self.assertEqual(af_tester.primes, [])
		primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
		for n in [1, 3, 4, 10]:
			af_tester.get_n_primes(n)
			self.assertEqual(af_tester.primes, primes[:n])
		with self.assertRaises(Exception):
			# Should raise a ValueError for any negative input
			af_tester.get_n_primes(-1)

	def test_word_intersection(self):
		word_intersection()
		with open(f"{ANAGRAM_FILE}\\intersect.txt") as intersect:
			# Intersect word list output depends on other word lists in directory,
			# so the only test is that the file exists and has words in it
			self.assertTrue(len(intersect.read().split()) > 0)


if __name__ == "__main__":
	unittest.main()
