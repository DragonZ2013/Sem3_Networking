import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("0.0.0.0",5555))
buff,addr=s.recvfrom(10)
print("Server Confirm")
ret_val=0
#while (
#	ret_val=ret_val+1
#print (str(buff[0])+" "+str(buff[1])+" "+str(buff[2])+" "+str(buff[3])+" "+str(buff[4]))
length = len(buff)
print(length)
length = str(length)
length = length.encode()
s.sendto(length,addr)
