import socket
try:
	s= socket.socket()
	host = socket.gethostname()
	port = 8889
	s.bind((host,port))
	s.listen(6)
	print "waiting request"
	print s.accept()
except Exception as err:
	print err
finally:
	s.close()
