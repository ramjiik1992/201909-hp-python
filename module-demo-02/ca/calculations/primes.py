
def is_prime(number):
    if number<2:return False

    for value  in range(2,number):
        if number%value==0:
            return False

    return True


def prime_range(min,max=None):
    if max is None:
        min,max=2,min
    
    primes=[]
    for value in range(min,max):
        if is_prime(value):
            primes.append(value)

    return primes
            

