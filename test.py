import unittest
from unittest import TestCase

from primes import get_n_primes
from pureanagram import encode_word
from words import get_all


class Test(TestCase):
    def test_get_n_primes(self):
        self.assertEqual(get_n_primes(0), [])
        self.assertEqual(get_n_primes(1), [2])
        self.assertEqual(get_n_primes(2), [2, 3])

    def test_get_all(self):
        self.assertEqual(get_all()[0], 'a')

    def test_encode_word(self):
        self.assertEqual(encode_word(""), 1)
        self.assertEqual(encode_word("a"), 2)
        self.assertEqual(encode_word("abc"), 30)
        self.assertEqual(encode_word("aBC"), 30)


if __name__ == "__main__":
    unittest.main()
