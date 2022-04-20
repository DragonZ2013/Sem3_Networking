import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
send_str=b"t"
send_bytes=bytearray(b'T')
s.sendto(send_str,("127.0.0.1",5555))
buff,addr=s.recvfrom(10)
print (buff)

