import threading as t
import time

class Counter(t.Thread):
    _count=0
    def __init__(self,max,name=None):
        t.Thread.__init__(self)
        self.max=max
        self.name= name if(name !=None) else 'Thread#'+Counter._count
        Counter._count+=1
    
    def run(self):
        print('{} started'.format(self.name))

        while self.max>=0:
            print('{} counted {}'.format(self.name,self.max))
            self.max-=1
            time.sleep(1)
        

c1=Counter(10,'Counter1')
c2=Counter(10,'Counter2')

c1.start()
c2.start()
print('waiting for thread to finish')

c1.join() #wait for this thread
c2.join() #wait for this thread

print('program ends...')






    

