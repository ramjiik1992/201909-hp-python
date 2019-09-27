import threading as t
import time

def count_down(name,max,sleep=0.1):
    print('{} started'.format(name))
    while max>=0:
        print('{} counts {}'.format(name,max))
        max-=1
        time.sleep(sleep)
    print('{} stopped'.format(name))



t1=t.Thread(target=count_down,args=('Vivek',20,0.2))
t2=t.Thread(target=count_down,args=('Vivek',10,0.5))

t1.start();
t2.start()

print('counter started...')
t1.join()
t2.join()
print('program ends...')






    

