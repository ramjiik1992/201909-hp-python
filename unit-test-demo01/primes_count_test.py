import unittest
from utils.primes import count_primes



class PrimeTest(unittest.TestCase):

    def test_there_are_4_primes_under_10(self):
        result=count_primes(0,10)
        self.assertEqual(4,result)

    def test_should_raise_valueError_for_wrong_range(self):
        self.assertRaises(ValueError, lambda : count_primes(10,1))        


if __name__=='__main__':
    unittest.main()


