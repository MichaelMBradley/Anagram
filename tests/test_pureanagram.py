import unittest
from unittest import TestCase

from src.pureanagram import anagrams_to_string, encode_word, encode_words_file, get_anagrams


encoded = encode_words_file("words_alpha")


class TestPureAnagram(TestCase):
	def test_anagrams_to_string(self):
		self.assertEqual(anagrams_to_string({}, "#"), "# -> # is an invalid character.")
		self.assertEqual(anagrams_to_string({}, "a"), "a -> no anagrams found.")
		self.assertEqual(anagrams_to_string({2: ["a"]}, "a"), "a -> no anagrams found.")
		self.assertEqual(anagrams_to_string({6: ["ab", "ba"]}, "ab"), "ab -> ba.")
		self.assertEqual(anagrams_to_string({30: ["abc", "acb", "bac", "bca", "cab", "cba"]}, "abc"),
																			"abc -> acb, bac, bca, cab, cba.")

	def test_encode_word(self):
		self.assertIsInstance(encode_word("a"), int)
		self.assertEqual(encode_word(""), 1)
		self.assertEqual(encode_word("a"), 2)
		self.assertEqual(encode_word("abc"), 30)
		self.assertEqual(encode_word("aBC"), 30)
		with self.assertRaises(ValueError):
			encode_word("_")

	def test_encode_words_file(self):
		self.assertIsInstance(encoded, dict)
		self.assertEqual(encoded[2], ["a"])

	def test_get_anagrams(self):
		self.assertIsInstance(encoded, dict)
		test_encoded = get_anagrams(encoded, "this")
		self.assertTrue("hits" in test_encoded)
		self.assertTrue("shit" in test_encoded)
		self.assertTrue("this" in test_encoded)
		with self.assertRaises(ValueError):
			get_anagrams(encoded, "")
		with self.assertRaises(ValueError):
			get_anagrams(encoded, "a")
		with self.assertRaises(ValueError):
			get_anagrams(encoded, "yu")


if __name__ == "__main__":
	unittest.main()
