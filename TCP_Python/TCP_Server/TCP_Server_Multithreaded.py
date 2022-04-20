import time
import socket
from threading import Thread
def f(cs,i):
	print("Processing client "+str(i))
	b=cs.recv(100)
	a=b.split(",")
	res=0
	for x in a:
		res+=int(x)
	res=res/len(a)
	time.sleep(3)
	cs.send(str(res))
	cs.close()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",7777))
s.listen(20)
i=0
while(1==1):
	i=i+1
	cs,addr=s.accept()
	print(addr)
	t=Thread(target=f,args=(cs,i))
	t.start()
