import time


def measure_performance(fn):
    def inner(*args,**kwargs):
        start=time.perf_counter()
        result=fn(*args,**kwargs)
        end=time.perf_counter()
        print(f'Total time taken is {end-start}')
        return result
        
    return inner