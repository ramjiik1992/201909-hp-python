import threading

def count_down():
    max=20
    t=threading.currentThread()
    print(f'{t.name} starts')
    while max>0:
        print(f'{t.name} counts {max}')
        max-=1

    print(f'{t.name} ends')
    

def main():
    t1=threading.Thread(target=count_down)
    t2=threading.Thread(target=count_down)

    t1.start()
    t2.start()

    print('end of program')    


if __name__=='__main__':
    main()