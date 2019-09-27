import threading
import time

def critical_task():
    print('critical task started')
    time.sleep(5)
    print('crtical task completed')

def non_critical_task():
    print('non critical task started')
    time.sleep(10)
    print('non crtical task completed')



def main():
    t1=threading.Thread(target=critical_task)
    t2=threading.Thread(target=non_critical_task)

    t2.setDaemon(True) # non critcal . must be set before start

    t1.start()
    t2.start()

    t1.join()
    #t2.join() # ---> no need to wait for non-critical thread

    print('end of program')    



if __name__=='__main__':
    main()