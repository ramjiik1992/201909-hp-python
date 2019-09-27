import threading

def main():
    t=threading.currentThread()
    print('current thread is ',t)
    print('name is ',t.name)
    


if __name__=='__main__':
    main()