import socket
try:
	s = socket.socket()
	#s.connect(('www.google.com',80))
	#s.connect(('www.google.com',443))
	port = 8889
	host = socket.gethostname()
	s.connect((host,port))
	print "connected"
except Exception as err:
	print err 
finally:
	s.close()