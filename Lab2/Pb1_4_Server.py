import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("0.0.0.0",5555))
buff,addr=s.recvfrom(10)
print("Server Confirm")

length = len(buff)
ret_val=length
for i in range(length):
	if  buff[i] in [65,69,73,79,85,97,101,105,111,117]:
		ret_val=ret_val-1
print(ret_val)
ret_val = str(ret_val)
ret_val = ret_val.encode()
s.sendto(ret_val,addr)
