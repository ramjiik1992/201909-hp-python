import threading

def count_down(id,max):
    
    t=threading.currentThread()
    print(f'{t.name}->{id} starts')
    while max>0:
        print(f'{t.name} counts {max}')
        max-=1

    print(f'{t.name}->{id} ends')
    

def main():
    t1=threading.Thread(target=count_down,args=(1,20))
    t2=threading.Thread(target=count_down,args=(2,30))

    t1.start()
    t2.start()

    print('end of program')    


if __name__=='__main__':
    main()