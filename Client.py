import socket
from os import listdir

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
print('connected to the remote server:',socket.gethostname(),'port 1234')


print('server is listening')
while True:

    print('--------------------------------------------')
    print('Make your choice')
    print('1)List : list of all the files in system')
    print('2)Read : Read the specified file')
    print('--------------------------------------------')
    client_input = int(input('enter a your choice'))
    if client_input == 1:
        Flist = [f for f in listdir('C:/Users/Ishan/Desktop')]
        print(Flist)
    if (client_input == 2):
        i = input('enter a filename')
        f = open('C:/Users/Ishan/Desktop/%s' % i, 'r')
        for x in f:
            print(x)
