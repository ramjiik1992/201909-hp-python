
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
            

def test():

    print('testing',__name__)

    test_data={2:True, 9:False, -3:True, -10:False, 0:False, 1:True}

    errors=0
    for (number,expected) in test_data.items():
        actual=is_prime(number)
        if actual!=expected:
            print('is_prime({}) failed. expected {} actual {}'.format(number,expected,actual))
            errors+=1

    if not errors:
        print('all test passed')
    else:
        print('{}/{} test failed'.format(errors, len(test_data)))

if __name__=='__main__':
    test()





