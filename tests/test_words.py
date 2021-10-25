import unittest
from unittest import TestCase

from src.words import ANAGRAM_FILE, get_words, get_n_primes, word_intersection


class TestWords(TestCase):
	def test_get_n_primes(self):
		self.assertIsInstance(get_n_primes(3), list)
		self.assertEqual(get_n_primes(0), [])
		self.assertEqual(get_n_primes(1), [2])
		self.assertEqual(get_n_primes(2), [2, 3])
		with self.assertRaises(Exception):
			get_n_primes(-1)

	def test_get_all(self):
		words = get_words("words_alpha")
		self.assertIsInstance(words, list)
		self.assertEqual(words[0], "a")

	def test_word_intersection(self):
		word_intersection()
		with open(f"{ANAGRAM_FILE}\\intersect.txt") as intersect:
			self.assertTrue(len(intersect.read().split()) > 0)


if __name__ == "__main__":
	unittest.main()
