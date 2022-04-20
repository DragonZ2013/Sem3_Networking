import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(b"hey",("127.0.0.1",6666))
print (s.recvfrom(10))
