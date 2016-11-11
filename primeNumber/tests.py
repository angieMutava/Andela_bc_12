import unittest
import primegenerator as testcases

class prime_checker(unittest.TestCase):

    def test_negative_numbers(self):
        self.assertEqual(testcases.prime_generator(-5), "Negative numbers not allowed.")

    def test_prime_generator(self):
        self.assertEqual(testcases.prime_generator(10), [2, 3, 5, 7])

    def test_int(self):
        self.assertEqual(testcases.prime_generator("str"), "Only integers allowed")

    def test_number_one(self):
        self.assertEqual(testcases.prime_generator(1), [])

    def test_number_zero(self):
        self.assertEqual(testcases.prime_generator(0), [])

    def test_prime_numbers_100(self):
        self.assertEqual(testcases.prime_generator(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_prime_50(self):
        self.assertEqual(testcases.prime_generator(50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

  

