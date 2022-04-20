import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("0.0.0.0",5555))
buff,addr=s.recvfrom(10)
print(addr)
ret_val=0

length = len(buff)
print(length)
length = str(length)
length = length.encode()
s.sendto(length,addr)
