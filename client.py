
import socket
import sys

HOST  = 'localhost'
PORT  = 50007
BDATA = bytes("https://i.imgur.com/VzsuCec.jpg", 'utf-8')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
s.send(BDATA)

reply = s.recv(1024)
print(reply.decode())
s.close()
