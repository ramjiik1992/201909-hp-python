import threading
import time
from utils import measure_performance
from threadutils import Task

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

@measure_performance
def permutation_mt(n,r):
    fn=threading.Thread(target=factorial,args=(n,))
    fn_r=threading.Thread(target=factorial,args=(n-r,))

    fn.start()
    fn_r.start()

    return fn/fn_r

@measure_performance
def permutation_task(n,r):
    fn=Task(factorial,n)
    fn_r=Task(factorial,n-r)

    
    return fn.result/fn_r.result



def main():
    n=7
    r=3
    p=permutation_task(n,r)
    print(f'{n}P{r}={p}')



if __name__=='__main__':
    main()