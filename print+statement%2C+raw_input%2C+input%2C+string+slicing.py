
# coding: utf-8

# In[1]:

a=raw_input('Enter a value:')
b=raw_input("Enter b value:")


# In[2]:

print a


# In[3]:

print b


# In[4]:

print type(a)


# In[5]:

c1=1+2j


# In[6]:

print type(c1)


# In[7]:

c1=1+2j
c2=2+4j
print c1+c2
print c1*c2
print c1-c2
print c1/c2


# In[8]:

a=raw_input('Enter a value:')


# In[9]:

print type(a)


# In[10]:

a=input("Enter a value: ")


# In[11]:

print type(a)


# In[12]:

s1 = "python"


# In[13]:

a=input("Enter a value: ")


# In[14]:

print type(a)


# In[15]:

print z


# In[16]:

a=input("Enter a value: ")


# In[18]:

a=input("Enter a value: ")
b=input("Enter b value: ")
print a+b


# In[19]:

a=input("Enter a value: ")
b=input("Enter b value: ")
print a+b


# In[21]:

name = "Anil"
age =23
height =5.6
print name,age,height


# In[22]:

# Name: Anil, Age: 23, height: 5.6
print "Name: "+name


# In[24]:

print "Name: "+name+", Age:"+age+", Height: "+height


# In[26]:

print "Name: "+name+", Age:"+str(age)+", Height: "+str(height)


# In[27]:

print "Name:",name


# In[29]:

print "Name:",name,", Age:",age,", Height:",height


# In[30]:

'''
line1
line2
'''
print "line1"
print "line2"


# In[31]:

print "line1\nline2"


# In[32]:

s="python program"
print len(s)


# In[33]:

s="python program\n"
print len(s)


# In[34]:

print "line1\nline2\ttabspace"


# In[35]:

# %s %d %f %r


# In[36]:

print "\n\t"


# In[37]:

print "%s%d%f%r"


# In[38]:

print "%s%d%f%r",('str1',10,1.2,(1,2,34))


# In[39]:

print "%s%d%f%r"%('str1',10,1.2,(1,2,34))


# In[40]:

print "%s,->%d,->%f,->%r"%('str1',10,1.2,(1,2,34))


# In[41]:

# Name: Anil, Age: 23, height: 5.6
print "Name: %s, Age: %d, height: %f"%(name,age,height)


# In[42]:

name="dfdsfsd"


# In[43]:

name=10


# In[45]:

# Name: Anil, Age: 23, height: 5.6
name="Anil"
print "Name: %r, Age: %r, height: %r"%(name,age,height)


# In[46]:

# it's a cool day
print "it's a cool day"


# In[47]:

print 'it's a cool day'


# In[48]:

print 'it\'s a cool day'


# In[49]:

# line1\nline2

print "line1\nline2"


# In[50]:

# line1\nline2

print "line1\\nline2"


# In[51]:

comment = "dsfsdfs\n\dsfds\t dsfdsf \t sfdsf\nsfsdf\t"
print comment


# In[52]:

comment = r"dsfsdfs\n\dsfds\t dsfdsf \t sfdsf\nsfsdf\t"
print comment


# In[53]:

s="line1\nline2\ttabspace"
print len(s)
s=r"line1\nline2\ttabspace" 
print len(s)


# In[54]:

s1="python program"


# In[55]:

print s1[0]


# In[56]:

print s1[12]


# In[58]:

print len(s1)


# In[59]:

print s1[20]


# In[60]:

s1


# In[61]:

print s1[0]+s1[1]+s1[2]


# In[63]:

print s1[0:3] # m:n  mth index to n-1th iindex


# In[64]:

s1


# In[66]:

print s1[len(s1)-1]


# In[67]:

s="python program"


# In[68]:

s


# In[69]:

print s[-1]


# In[70]:

print s[-3]


# In[71]:

s


# In[72]:

print s[0:6]


# In[73]:

print s[:6]


# In[74]:

print s[6:]


# In[75]:

print s[3:7]


# In[76]:

print s[7:3]


# In[77]:

s


# In[78]:

print s[0:12:2]


# In[79]:

print s[7:3:-1]


# In[80]:

print s[::-1]


# In[81]:

s


# In[82]:

s="python"
s1=s
s2=s[:]


# In[83]:

print s,s1,s2


# In[84]:

print id(s),id(s1),id(s2)


# In[85]:

print s[0]


# In[86]:

s[0] = "z"


# In[87]:

i=1023456


# In[88]:

print i[0:2]


# In[ ]:

print "program started"
def fun(){
    print "statements in function"
}
    


# In[89]:

print "program started"
def fun():
    print "function started"
    print "statements in function"
    print "function ended"
print "other statements in program"
fun()
print "program ended"
    

    


# In[90]:

print "program started"
def fun():
    print "function started"
    print "statements in function"
print "function ended"
print "other statements in program"
fun()
print "program ended"
    

    


# In[91]:

print "program started"
def fun():
    print "function started"
    print "statements in function"
  print "function ended"
print "other statements in program"
fun()
print "program ended"
    


# In[92]:

print "program started"
def fun():
  print "function started"
  print "statements in function"
  print "function ended"
print "other statements in program"
fun()
print "program ended"
    


# In[93]:

print "program started"
def fun():
  print "function started"
    print "statements in function"
  print "function ended"
print "other statements in program"
fun()
print "program ended"
    


# In[94]:

print "program started"
def fun():
  print "function started"
print "statements in function"
  print "function ended"
print "other statements in program"
fun()
print "program ended"
    


# In[95]:

print "program started"
def fun():
  print "function started"
  print "statements in function"
  print "function ended"
def fun2():
    print "fun2 definition"
print "other statements in program"
fun()
print "program ended"
    


# In[96]:

print "program started"
def fun():
    print "this is finction"
print "program ended"


# In[97]:

print "program started"
def fun():
    print "this is finction"
fun()
print "program ended"


# In[98]:

print "program started"
def fun():
    print "this is finction"
print "program ended"
fun()


# In[99]:

def fun(a,b):
    print a+b
fun(10,20)
    


# In[100]:

def fun(a,b):
    c = a+b
fun(10,20)


# In[101]:

def fun(a,b):
    c = a+b
    print c
d = fun(10,20)
print "d=",d


# In[102]:

d


# In[103]:

print d


# In[104]:

print type(d)


# In[105]:

s1=python


# In[106]:

s1=None


# In[107]:

s1=True


# In[108]:

print type(s1)


# In[ ]:



