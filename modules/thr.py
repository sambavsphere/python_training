from threading import Thread
from time import sleep
def fun1():
	for i in range(10):
		print i
		sleep(1)

def fun():
	print "therad1 started"
	t1 = Thread(target=fun1)
	t1.start()
	return t1
print "program started"
t = fun()
sleep(2)
print "stoping thread"
t.stop()
print "program ended"

