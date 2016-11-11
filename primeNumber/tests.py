import unittest
import primegenerator

class prime_checker(unittest.TestCase):

	def test_negative_numbers(self):
		self.assertEqual(prime_generator(-5), "Negative numbers not allowed.")

	def test_prime_generator(self):
		self.assertEqual(prime_generator(10), [2, 3, 5, 7])

	def test_data_type(self):
		self.assertEqual(prime_generator("str"), "Number should be integer")

