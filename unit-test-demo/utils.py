
import math

def is_prime(number):
    '''
    >>> is_prime(29)
    True

    >>> is_prime(23)
    True

    >>> is_prime(-7)
    False

    >>> is_prime(2)
    True
    '''
    #if number<0 : number*=-1
    if number<2 : return False

    for d in range(2,number):
        if number % d==0:
            return False
    
    return True


def prime_count(min,max):
    count=0
    for n in range(min,max):
        if is_prime(n):
            count+=1

    return count

