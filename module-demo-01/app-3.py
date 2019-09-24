'''
1. Accept min and max from the User
2. Find All Primes in the range
3. Find Their sum and average and min,max
4. Print The Result
'''

#import primes as p  #import object and name it as 'p'

#imports a single name in the global space
# module object primes in not available
from primes import prime_range 

#import all names from maths module
#but not the module maths itself
from  maths import sum,average  # we know what we are importing

def main():
    lo=50 #int(input('min?'))
    hi=100 #int(input('max?'))

    #no need (or option) to qualify the name with p.
    primes=prime_range(lo,hi) #from primes.py

    #no need to qualify sum and average
    s=sum(*primes)    #overwrites builtin sum function  with my function
    a=average(*primes)  
    lowest=min(primes)  #not importing min from maths.py. using builtin function
    highest=max(primes) 

    print('results');


    print('primes are ',primes)
    print('sum is ',s)
    print('average is ',a)
    print('lowest is ',lowest)
    print('higest is ',highest)

main()