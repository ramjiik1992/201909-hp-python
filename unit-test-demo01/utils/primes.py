def is_prime(value):
    '''
    Checks if a given number is prime or not
    Returns True|False

    >>> is_prime(0)
    False

    >>> is_prime(2)
    True

    >>> is_prime(-7)
    False

    >>> is_prime(13)
    True

    '''

    if value<2: return False
    
    for test in range(2,value):
        if value%test==0:
            return False
    return True


def count_primes(min,max):
    '''
    counts prime in a given min max range
    >>> count_primes(0,10)
    4
    >>> count_primes(0,100)
    25
    '''
    if max<min:
        raise ValueError(f'invalid range max[{max}] should be greater than min[{min}]')
    count=0
    for i in range(min,max):
        if is_prime(i):
            count+=1

    return count