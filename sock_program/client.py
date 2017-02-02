import socket
s=socket.socket()
import json
try:
	s.connect((socket.gethostname(),8889))
	ack = s.recv(1024)
	print ack
	# emp_id = raw_input("Enter an empid:")
	# s.send(emp_id)
	# data =  s.recv(1024)
	# print data
	# print type(data)
	# data  =json.loads(data)
	# print type(data)
except Exception as err:
	print err
finally:
	s.close()
