import unittest
from unittest import TestCase

from src.pureanagram import anagrams_to_string, encode_word, encode_words_file, get_anagrams
from src.words import InvalidCharacterException, NoAnagramsException


class TestPureAnagram(TestCase):
    def test_anagrams_to_string(self):
        self.assertEqual(anagrams_to_string({}, "#"), "# contains an invalid character, '#'.")
        self.assertEqual(anagrams_to_string({}, "a"), "a -> a has no known anagrams.")
        self.assertEqual(anagrams_to_string({2: ["a"]}, "a"), "a -> a has no known anagrams.")
        self.assertEqual(anagrams_to_string({6: ["ab", "ba"]}, "ab"), "Ba.")
        self.assertEqual(anagrams_to_string({30: ["abc", "acb", "bac", "bca", "cab", "cba"]}, "abc"),
                         "Acb, bac, bca, cab, cba.")

    def test_encode_word(self):
        self.assertIsInstance(encode_word("a"), int)
        self.assertEqual(encode_word(""), 1)
        self.assertEqual(encode_word("a"), 2)
        self.assertEqual(encode_word("abc"), 30)
        self.assertEqual(encode_word("aBC"), 30)
        with self.assertRaises(InvalidCharacterException):
            encode_word("_")

    def test_encode_words_file(self):
        encoded = encode_words_file()
        self.assertIsInstance(encoded, dict)
        self.assertEqual(encoded[2], ["a"])

    def test_get_anagrams(self):
        encoded = encode_words_file()
        self.assertIsInstance(encoded, dict)
        self.assertEqual(get_anagrams(encoded, "this"), ["hist", "hits", "isth", "shit", "sith", "this", "tshi"])
        with self.assertRaises(NoAnagramsException):
            get_anagrams(encoded, "")
        with self.assertRaises(NoAnagramsException):
            get_anagrams(encoded, "a")
        with self.assertRaises(NoAnagramsException):
            get_anagrams(encoded, "yu")


if __name__ == "__main__":
    unittest.main()
