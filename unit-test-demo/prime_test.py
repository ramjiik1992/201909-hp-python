import unittest
from utils import is_prime

class PrimeTest(unittest.TestCase):
    def test_negative_numbers_are_not_prime(self):
        self.assertFalse(is_prime(-2),'negative number shouldnt be prime')
        self.assertFalse(is_prime(-6),'negative number shouldnt be prime')
        self.assertFalse(is_prime(-7),'negative number shouldnt be prime')

    def test_2_is_prime(self):
        self.assertTrue(is_prime(2))
        

    def test_22_is_not_prime(self):
        self.assertFalse(is_prime(22))

    def test_23_is_prime(self):
        self.assertTrue(is_prime(23))

    def test_22_is_not_prime(self):
        self.assertFalse(is_prime(22))
    

if __name__ == '__main__':
    unittest.main()