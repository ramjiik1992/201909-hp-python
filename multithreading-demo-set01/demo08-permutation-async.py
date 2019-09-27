import threading
import time
from utils import measure_performance
from threadutils import asynchronous

@asynchronous
def factorial(n):
    fn=1
    for x in range(1,n+1):
        fn*=x
        time.sleep(1)

    return fn

@measure_performance
def permutation_async(n,r):
    fn=factorial(n)
    fn_r=factorial(n-r)

    return fn.result/fn_r.result




def main():
    n=7
    r=3
    p=permutation_async(n,r)
    print(f'{n}P{r}={p}')



if __name__=='__main__':
    main()