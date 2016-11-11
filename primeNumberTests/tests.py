import unittest
from primeNumber import prime_generator

class prime_checker(unittest.TestCase):

	def test_negative_numbers(self):
		self.assertEqual(prime_generator(-5), "Negative numbers not allowed.")

	def test_prime_generator(self):
		self.assertEqual(prime_generator(10), [2, 3, 5, 7])
