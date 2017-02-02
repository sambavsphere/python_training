import socket
import db_script
import json
s=socket.socket()
try:
	s.bind((socket.gethostname(),8889))
	s.listen(6)
	print "waiting for request"
	cobj,cinfo= s.accept()
	cobj.send("connecion established successfully!")
	# emp_id= cobj.recv(1024)
	# record = db_script.browse(emp_id)
	# cobj.send(json.dumps(record))

except Exception as err:
	print err
finally:
	s.close()
