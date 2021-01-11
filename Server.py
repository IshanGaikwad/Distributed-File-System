import socket
from os import listdir

port = 1234
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('10.0.0.160', port))
#s.listen(5)
i=0

    

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('10.0.0.160', port))
    s.listen(5)
    clientsocket, address = s.accept()
    print("connection ",i)
    print(f"Connection from {address} has been established.")
    msg = clientsocket.recv(1024)
    msg = msg.decode("utf-8")
    print(msg)
    if msg == 'list':
        test=''
        Flist = [f for f in listdir('C:/Users/Ishan/Desktop')]
        for x in Flist:
            test+=x+'\n'
            print(x)
        #clientsocket.send(bytes('\0','utf-8'))
        clientsocket.send(bytes(test,'utf-8'))
    elif msg == 'read':
        clientsocket.send(bytes("enter the name of file",'utf-8'))
        msg1 = clientsocket.recv(1024)
        msg1 = msg1.decode('utf-8')
        f = open('C:/Users/Ishan/Desktop/%s' % msg1, 'r')
        for x in f:
            print(x)
    i+=1
    s.close()
