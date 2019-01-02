
import socket
import subprocess
from main import *

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

#cnt = 0
while(1):
    s.listen(1)

    conn, addr = s.accept()
    print('Connected by', addr)
    
    tst = open("Output.txt",'r')
    while 1:
        data = conn.recv(1024)
        if data:
            print(data)
            subprocess.run(["wget","-O","123.jpg",data])
            r = Receipt("123.jpg")
            r.main()
            Btst = tst.read().encode()
            conn.sendall(Btst)
        else:
            conn.close()
            tst.close()
            break
