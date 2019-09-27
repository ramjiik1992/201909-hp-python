import unittest
from utils.primes import is_prime


class PrimeTest(unittest.TestCase):

    def test_2_is_prime(self):
        self.assertEquals(True, is_prime(2))


    def test_evens_are_not_prime(self):
        self.assertFalse( is_prime(4))
        self.assertFalse(is_prime(8))


    def test_13_is_prime(self):
        self.assertTrue(is_prime(13))


    def test_negatives_are_notprime(self):
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(-7))

if __name__=='__main__':
    unittest.main()


