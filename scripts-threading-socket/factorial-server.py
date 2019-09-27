import socket
import sys
import threading
from threading import Thread

# python 3 requirement for ensuring unicode data is transferred as binary
def send(socket,message):
    socket.sendall('{0}'.format(message).encode())

def recv(socket):
    return socket.recv(1024).decode('utf_8')

def factorial(n):
    if(n<2) : return 1
    else: return n*factorial(n-1)


def talkToClient(client):
    message=None
    try:
        while True:
            #data= client.recv(1024)
            #message=str(data).lower()
            
            message=recv(client).lower().strip()

            print('client:{}'.format(message))
            if(message=='bye'): 
                #client.send('bye')
                send(client,'bye')
                return;
            if(message=='__kill__'):
                send(client,'bye')
                sys.exit(0)
                
            try:
                value=int(message)
                result=factorial(value)
                #client.send('{}'.format(result))
                send(client,result)
            except:
                #client.send('invalid request {}'.format(message))
                send(client,'invalid request {}'.format(message))
    except:
        return

def main():
    args=sys.argv
    port=9200
    server='localhost'
    if len(args)>1: port=int(args[1])
    if len(args)>2: server=args[2]

    print('starting server on {} : {} '.format(server,port))
    s=socket.socket()
    s.bind((server,port))  # server should reserve a port on a server where it will connect with the client
    s.listen(1)  # now I am ready for the request

    print('server started...')

    while True:
        print('waiting for the client...')
        (client,addr)=s.accept()  #accept incoming request or wait indefinitely
        print('connected to {}'.format(addr))
        t=Thread(target=talkToClient,args=(client,))
        t.start()
        


if __name__=='__main__' : main()