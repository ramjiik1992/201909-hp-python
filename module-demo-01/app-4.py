
import primes as p

from  maths import sum,average  

def main():
    #print(dir(p)) # lets see what is present in p
    print('welcome to the program...',__name__)
    lo=int(input('min?'))
    hi=int(input('max?'))

    #no need (or option) to qualify the name with p.
    primes=p.prime_range(lo,hi) #from primes.py

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


if __name__=='__main__':
    main()