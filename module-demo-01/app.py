'''
1. Accept min and max from the User
2. Find All Primes in the range
3. Find Their sum and average and min,max
4. Print The Result
'''

import primes as p  #import object and name it as 'p'
import maths # as maths

def main():
    lo=int(input('min?'))
    hi=int(input('max?'))

    primes=p.prime_range(lo,hi) #from primes.py
    s=maths.sum(*primes)      #from math.py
    a=maths.average(*primes)  #from math.py
    lowest=min(primes)  # python function
    highest=max(primes) # python function

    print('primes are ',primes)
    print('sum is ',s)
    print('average is ',a)
    print('lowest is ',lowest)
    print('higest is ',highest)

main()