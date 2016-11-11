import unittest
import primegenerator as testcases

class prime_checker(unittest.TestCase):

    def test_negative_numbers(self):
        self.assertEqual(testcases.prime_generator(-5), "Negative numbers not allowed.")

    def test_prime_generator(self):
        self.assertEqual(testcases.prime_generator(10), [2, 3, 5, 7])

    def test_data_type(self):
        self.assertEqual(testcases.prime_generator("str"), "Only integers allowed")

    def test_number_one(self):
    	self.assertEqual(testcases.prime_generator(1), [])
    def test_number_zero(self):
    	self.assertEqual(testcases.prime_generator(0), [])
