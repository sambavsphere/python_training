from threading import Thread
from time import sleep
def dir_failre():
	for i in range(10):
		print "failing director"
		sleep(2)
def pass_io():
	for i in range(20):
		print "passing io"
		sleep(2)
dirf = Thread(target=dir_failre)
pio = Thread(target=pass_io)
dirf.start()
pio.start()
while True:
	if not dirf.isAlive():
		break
while True:
	if not pio.isAlive():
		break	 
print "*"*20
print "end of the program"
