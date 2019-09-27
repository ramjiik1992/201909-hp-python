import threading

class CountDownTask(threading.Thread):
    def __init__(self, id,max,autoStart=True):
        super().__init__()
        self.id=id
        self.max=max
        if autoStart:
            self.start()

    def start(self):
        if not self.is_alive():
            super().start()

    def run(self):
        id=self.id
        max=self.max
        t=threading.currentThread()
        print(f'{t.name}->{id} starts')
        while max>0:
            print(f'{t.name} counts {max}')
            max-=1

        print(f'{t.name}->{id} ends')
    

def main():
    t1=CountDownTask(1,20,False)
    t2=CountDownTask(2,30) #no auto start

    
    t1.start() # need manual start
    t2.start() # you can't restart a thread

    t1.join() # main thread waits for t1 to finish
    t2.join()
    print('end of program')    


if __name__=='__main__':
    main()