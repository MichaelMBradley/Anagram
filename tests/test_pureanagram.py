import unittest
from unittest import TestCase

from src.pureanagram import PureAnagram


pa_tester = PureAnagram("words_alpha")


class TestPureAnagram(TestCase):
	def test_anagrams_to_string(self):
		# Ensure that output is formatted properly
		self.assertIsInstance(pa_tester.anagrams_to_string(""), str)
		# While this could be cleaned up with a loop, it would almost certainly look messier
		self.assertEqual(pa_tester.anagrams_to_string("#"), "# -> not in [a, z] | [A, Z].")
		self.assertEqual(pa_tester.anagrams_to_string("a"), "a -> no anagrams found.")
		self.assertEqual(pa_tester.anagrams_to_string("ab"), "ab -> ba.")
		self.assertEqual(pa_tester.anagrams_to_string("abc"), "abc -> bac, cab.")

	def test_encode_word(self):
		# Ensure that encoding is calculated correctly
		self.assertIsInstance(pa_tester.encode_word(""), int)
		correct_encodings = {"": 1, "a": 2, "abc": 30, "aBC": 30}
		for string in correct_encodings.keys():
			self.assertEqual(pa_tester.encode_word(string), correct_encodings[string])
		# Ensure that no non-alphabetical character gets through
		for bad_char in "_@[`{":
			with self.assertRaises(ValueError):
				pa_tester.encode_word(bad_char)

	def test_encode_words_file(self):
		self.assertIsInstance(pa_tester.encoded_words, dict)
		self.assertEqual(pa_tester.encoded_words[2], ["a"])

	def test_get_anagrams(self):
		self.assertIsInstance(pa_tester.encoded_words, dict)
		test_encoded = pa_tester.get_anagrams("this")
		for anagram in ["hits", "shit", "this"]:
			self.assertTrue(anagram in test_encoded)
		for bad_str in ["", "a", "yu"]:
			with self.assertRaises(ValueError):
				pa_tester.get_anagrams(bad_str)


if __name__ == "__main__":
	unittest.main()
