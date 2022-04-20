import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("0.0.0.0",7777))
buff,addr=s.recvfrom(20)
print (addr)
print (buff)
ret_val=0
for c in buff:
	if(c.isdigit()):
		ret_val+=int(c)

s.sendto(str(ret_val),addr)
