import utils

def test_2_is_prime():
    assert utils.is_prime(2)==True

def test_12_is_not_prime():
    assert not utils.is_prime(12)

def test_negatives_are_not_prime():
    assert utils.is_prime(-2)==False
    assert not utils.is_prime(-8)
    
def test_4_primes_under_10():
    assert utils.prime_count(0,10)==4

def test_25_primes_under_100():
    assert utils.prime_count(0,100)==25