import threading as t
import time

class Bag:
    def __init__(self):
        self._counter=0

    def add_item(self):
        self._counter+=1
    
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
    theBag=Bag()
    workerCount=int(input('worker count?'))
    itemsToAdd=int(input('items per worker? '))
    r=input('use same basket? ')
    useSameBasket= r=='y'

    for i in range(workerCount):
        bag= theBag if useSameBasket else Bag()
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

