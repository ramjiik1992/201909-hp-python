import threading
import time
from utils import measure_performance

def factorial(n):
    fn=1
    for x in range(1,n+1):
        fn*=x
        time.sleep(1)

    return fn

@measure_performance
def permutation(n,r):
    fn=factorial(n)
    fn_r=factorial(n-r)

    return fn/fn_r



def main():
    n=7
    r=3
    p=permutation(n,r)
    print(f'{n}P{r}={p}')



if __name__=='__main__':
    main()