import pdb
import mod1
import sys,os
print os.system('dir')
a=10
b=20
c=a+b
print c
def fun():
	print "function started"
	c1=10
	c2=30
	res=c1+c2
	return res

for i in range(1,3):
	print 10/i
pdb.set_trace()
print fun()
print mod1.fun1()
print "program ended"