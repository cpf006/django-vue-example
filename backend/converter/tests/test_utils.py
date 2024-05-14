from django.test import TestCase
from ..utils import number_to_words

class NumberToWordsTests(TestCase):
    def test_single_digits(self):
        self.assertEqual(number_to_words(0), "zero")
        self.assertEqual(number_to_words(7), "seven")

    def test_negative_single_digits(self):
        self.assertEqual(number_to_words(-1), "negative one")
        self.assertEqual(number_to_words(-9), "negative nine")

    def test_tens(self):
        self.assertEqual(number_to_words(10), "ten")
        self.assertEqual(number_to_words(21), "twenty one")

    def test_negative_tens(self):
        self.assertEqual(number_to_words(-10), "negative ten")
        self.assertEqual(number_to_words(-21), "negative twenty one")

    def test_large_numbers(self):
        self.assertEqual(number_to_words(1001), "one thousand one")
        self.assertEqual(number_to_words(123456), "one hundred twenty three thousand four hundred fifty six")

    def test_negative_large_numbers(self):
        self.assertEqual(number_to_words(-1001), "negative one thousand one")
        self.assertEqual(number_to_words(-123456), "negative one hundred twenty three thousand four hundred fifty six")

    def test_edge_cases(self):
        self.assertEqual(number_to_words(1000000), "one million")
        self.assertEqual(number_to_words(1000000000), "one billion")

    def test_negative_edge_cases(self):
        self.assertEqual(number_to_words(-1000000), "negative one million")
        self.assertEqual(number_to_words(-1000000000), "negative one billion")