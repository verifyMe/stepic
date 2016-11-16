import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1', 2222))
s.send('Hello!!'.encode('utf-8'))
rsp = s.recv(1024)
print(rsp.decode())
s.send('close'.encode('utf-8'))
#rsp = s.recv(1024)
#print(rsp.decode())