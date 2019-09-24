'''
1. Accept min and max from the User
2. Find All Primes in the range
3. Find Their sum and average and min,max
4. Print The Result
'''
import primes

def main():
    print(primes)
    print('type',type(primes))
    print('id',id(primes))
    # to see the internals of an object use dir
    print('contents',dir(primes))

    primeList=primes.prime_range(1,10)
    print(primeList)

main()