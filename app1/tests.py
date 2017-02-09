import app
# test1
obj = app.operations(10,20)
res =  obj.mul()
ideal_output = 200
if res == ideal_output:
	print "test1 passed"
else:
	print "test1 is failed"
obj1 = app.operations(4,"s")
res =  obj.mul()
ideal_output = "ssss"

if res == ideal_output:
	print "test2 passed"
else:
	print "test2 is failed"




