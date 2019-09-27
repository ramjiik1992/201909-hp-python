import threading as t
import time

class Bag:
    def __init__(self,lockRequired=False):
        self._counter=0
        self._lock = t.Lock() if lockRequired else None
        self.add_item= self._add if not lockRequired else self._add_locked

    def _add_locked(self):
        self._lock.acquire()
        self._add()
        self._lock.release()

    def _add(self):
        c=self._counter
        c+=1
        self._counter=c

    def get_items(self): return self._counter

    def __str__(self): return 'Bag({0})'.format(self._counter)






class Worker(t.Thread):
    
    def __init__(self,bag,workCount=1000):
        t.Thread.__init__(self)
        self.bag=bag
        self.workCount=workCount
        #print('worker created with bag =',self.bag)
        #self.run=False

    def run(self): 
        #print('starting the work with bag={0} and workcount={1}'.format(self.bag,self.workCount))       
        for c in range(self.workCount):
            self.bag.add_item()
        #print('ending the work')


    
def main():
    workers=[]
    
    workerCount=int(input('worker count?'))
    itemsToAdd=int(input('items per worker? '))
    r=input('use same basket? ')
    useSameBasket= r=='y'
    r=input('lock bag ? ')
    lockBag= r=='y'
    theBag=Bag(lockBag)

    for i in range(workerCount):
        bag= theBag if useSameBasket else Bag(lockBag)
        worker=Worker(bag,itemsToAdd)
        workers.append(worker)

    print('starting workers...')

    for worker in workers:
        worker.start()
    
    print('waiting for workers to finish...')

    for worker in workers:
        worker.join()

    print('stand by for result...')

    totalCount=0
    if useSameBasket:
        totalCount=theBag.get_items()
    else:
        for worker in workers:
            totalCount+=worker.bag.get_items()

    print('total items added was {}'.format(totalCount))

main()

