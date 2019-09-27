import socket
import sys


def send(socket,message):
    socket.sendall('{0}'.format(message).encode())

def recv(socket):
    return socket.recv(1024).decode('utf_8')


def main():
    args=sys.argv
    port=9200
    server='localhost'
    
    if len(args)>1: server=args[1]
    if len(args)>2: port=int(args[2])

    print('connecting to {} : {} '.format(server,port))
    s=socket.socket()
    s.connect((server,port)) 
    print('connected...')

    while True:
        message=input('? ')
        #s.send(message);
        send(s,message)
        #message=str(s.recv(1024))
        message=recv(s)
        print('>>{}'.format(message))
        if(message.lower()=='bye'):
            break;
        
    s.close()
    print('thanks for using the program!!!')

main()