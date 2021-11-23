import unittest
from unittest import TestCase

from src.crossword import CrosswordSolver
from src.words import AnagramError, LetterError


cw_tester = CrosswordSolver("words_alpha.txt")


class MyTestCase(TestCase):
	def test_test_anagrams_to_string(self):
		self.assertIsInstance(cw_tester.anagrams_to_string(""), str)
		self.assertEqual(cw_tester.anagrams_to_string("a"), str(AnagramError("a")))
		self.assertEqual(cw_tester.anagrams_to_string("."), str(LetterError(".")))
		self.assertEqual(
			cw_tester.anagrams_to_string("?"),
			"? -> a, b, c, d, e, f, g, h, i, y, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, z."
		)
		self.assertEqual(cw_tester.anagrams_to_string("th?s"), "th?s -> this, thos, thus.")
		self.assertEqual(cw_tester.anagrams_to_string("th?t"), "th?t -> that.")

	def test_encode_words(self):
		self.assertIsInstance(cw_tester.encode_word(""), int)
		# Could be replaced with a couple of lists and a loop, but probably better not to
		self.assertEqual(cw_tester.encode_word(""), 1)
		self.assertEqual(cw_tester.encode_word("?"), 1)
		self.assertEqual(cw_tester.encode_word("a"), 2)
		self.assertEqual(cw_tester.encode_word("a?"), 2)
		self.assertEqual(cw_tester.encode_word("z"), 101)
		self.assertEqual(cw_tester.encode_word("aa"), 206)
		self.assertEqual(cw_tester.encode_word("?a"), 103)
		self.assertEqual(cw_tester.encode_word("ab"), 214)

	def test_get_anagrams(self):
		self.assertIsInstance(cw_tester.encodings, dict)
		test_encoded = cw_tester.get_anagrams("th?s")
		for anagram in ["this", "thos", "thus"]:
			self.assertTrue(anagram in test_encoded)
		for bad_str in ["", "a", "yu", "this"]:
			with self.assertRaises(AnagramError):
				cw_tester.get_anagrams(bad_str)


if __name__ == '__main__':
	unittest.main()
