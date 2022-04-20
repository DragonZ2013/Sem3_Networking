import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
send_bytes=bytearray(b'Test')
s.sendto(send_bytes,("127.0.0.1",5555))
buff,addr=s.recvfrom(10)
print (buff)
