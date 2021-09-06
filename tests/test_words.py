import unittest
from unittest import TestCase

from src.words import get_all, get_n_primes


class TestWords(TestCase):
    def test_get_n_primes(self):
        self.assertIsInstance(get_n_primes(3), list)
        self.assertEqual(get_n_primes(0), [])
        self.assertEqual(get_n_primes(1), [2])
        self.assertEqual(get_n_primes(2), [2, 3])
        with self.assertRaises(Exception):
            get_n_primes(-1)

    def test_get_all(self):
        words = get_all()
        self.assertIsInstance(words, list)
        self.assertEqual(words[0], "a")


if __name__ == "__main__":
    unittest.main()
