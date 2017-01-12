
# coding: utf-8

# In[1]:

a=10
b=20
print a+b


# In[2]:

print a>b


# In[3]:

print a<b


# In[4]:

print a<=b


# In[5]:

print a>=b


# In[6]:

print a==b


# In[7]:

print a is b


# In[8]:

print "sub" in "actual substring"


# In[9]:

a=10
b=a


# In[10]:

a==b


# In[11]:

a is b


# In[12]:

a=10
b=10


# In[13]:

a is b


# In[14]:

l1=[1,2,3,4]
l2=[1,2,3,4]


# In[15]:

l1 == l2


# In[16]:

l1 is l2


# In[17]:

def fun(a,b):
    a=10+a
    b=100+b
    print a+b
    return "return value"
c=fun(10,20)
print "c=",c


# In[18]:

def fun(a,b):
    a=10+a
    b=100+b
    return a+b
c=fun(10,20)
print "c=",c


# In[19]:

c=bool(10>20)


# In[20]:

c


# In[21]:

a=10
b=20


# In[22]:

10>"2"


# In[23]:

"1">100


# In[24]:

"12"<"2"


# In[25]:

"12", "2","012","1000"


# In[26]:

bool(0)


# In[27]:

bool(10>20)


# In[28]:

bool(0)


# In[29]:

bool(-10)


# In[30]:

bool(10)


# In[31]:

bool("python")


# In[32]:

bool("")


# In[33]:

bool("0")


# In[34]:

10<20 and 1<2


# In[35]:


10<20 and 1>2


# In[37]:

10<20 or 1>2


# In[38]:

# if if else if else if


# In[39]:

print "program strted"
if 10>20:
    print "if block started"
    print "10>20 is True"
    print "if block ended"
else:
    print "else block started"
    print "10>20 is False"
    print "end of else block"

print "other sttements in program"
print "program ended"


# In[40]:

'''
Menu:
1. windows
2. Linux
3. Mac
'''
print "Menu:\n1. Windows\n2. Linux\n3. Mac"


# In[41]:

'''
Menu:
1. windows
2. Linux
3. Mac
'''
print "Menu:\n1. Windows\n2. Linux\n3. Mac"
opt = raw_input("Enter an option: ")


# In[42]:

opt


# In[44]:

'''
Menu:
1. windows
2. Linux
3. Mac
'''
print "program started"
print "Menu:\n1. Windows\n2. Linux\n3. Mac"
opt = raw_input("Enter an option: ")

if opt == "1":
    print "windows selected"
if opt == "2":
    print "Linux selected"
if opt =="3":
    print "Mac selected"
    

print "other statements in program"
print "program ended"


# In[45]:

'''
Menu:
1. windows
2. Linux
3. Mac
'''
print "program started"
print "Menu:\n1. Windows\n2. Linux\n3. Mac"
opt = raw_input("Enter an option: ")

if opt == "1":
    print "windows selected"
if opt == "2":
    print "Linux selected"
if opt =="3":
    print "Mac selected"
    

print "other statements in program"
print "program ended"


# In[46]:

'''
Menu:
1. windows
2. Linux
3. Mac
'''
print "program started"
print "Menu:\n1. Windows\n2. Linux\n3. Mac"
opt = raw_input("Enter an option: ")

if opt == "1":
    print "windows selected"
if opt == "2":
    print "Linux selected"
if opt =="3":
    print "Mac selected"
    

print "other statements in program"
print "program ended"


# In[47]:

'''
Menu:
1. windows
2. Linux
3. Mac
'''
print "program started"
print "Menu:\n1. Windows\n2. Linux\n3. Mac"
opt = raw_input("Enter an option: ")

if opt == "1":
    print "windows selected"
if opt == "2":
    print "Linux selected"
if opt =="3":
    print "Mac selected"
    

print "other statements in program"
print "program ended"


# In[48]:

'''
Menu:
1. windows
2. Linux
3. Mac
'''
print "program started"
print "Menu:\n1. Windows\n2. Linux\n3. Mac"
opt = raw_input("Enter an option: ")

if opt == "1":
    print "windows selected"
if opt == "2":
    print "Linux selected"
if opt =="3":
    print "Mac selected"
else:
    print "wrong option selected"
    

print "other statements in program"
print "program ended"


# In[49]:

'''
Menu:
1. windows
2. Linux
3. Mac
'''
print "program started"
print "Menu:\n1. Windows\n2. Linux\n3. Mac"
opt = raw_input("Enter an option: ")

if opt == "1":
    print "windows selected"
elif opt == "2":
    print "Linux selected"
elif opt =="3":
    print "Mac selected"
else:
    print "wrong option selected"
    

print "other statements in program"
print "program ended"


# In[50]:

'''
Menu:
1. windows
2. Linux
3. Mac
'''
print "program started"
print "Menu:\n1. Windows\n2. Linux\n3. Mac"
opt = raw_input("Enter an option: ")

if opt == "1":
    print "windows selected"
elif opt == "2":
    print "Linux selected"
elif opt =="3":
    print "Mac selected"
else:
    print "wrong option selected"
    

print "other statements in program"
print "program ended"


# In[51]:

#looping statements
# for while


# In[ ]:

print "program started"
i=0
while i<10:
    print "iteration started"
    print i
    print "iteration ended"

print "other statements in program"
print "program ended"


# In[52]:

print "program started"
i=0
while i<3:
    print "iteration started"
    print i
    i=i+1
    print "iteration ended"

print "other statements in program"
print "program ended"


# In[53]:

print "program started"
for i in "abc":
    print "iteration started"
    print i
    print "iteration ended"

print "other statements in program"
print "program ended"


# In[54]:

# looping control statements: break continue


# In[55]:

print "program started"
s=raw_input("Enter sequence to iterate: ")
for i in s:
    print "iteration started"
    print i
    print "iteration ended"

print "other statements in program"
print "program ended"


# In[56]:

print "program started"
s=raw_input("Enter sequence to iterate: ")
for i in s:
    print "iteration started"
    print i
    if i == " ":
        break
    print "iteration ended"

print "other statements in program"
print "program ended"


# In[57]:

print "program started"
s=raw_input("Enter sequence to iterate: ")
for i in s:
    print "iteration started"
    if i == " ":
        break
    print i
    print "iteration ended"

print "other statements in program"
print "program ended"


# In[59]:

print "program started"
s=raw_input("Enter sequence to iterate: ")
for i in s:
    print "iteration started"
    print i
    print "iteration ended"
    continue

print "other statements in program"
print "program ended"


# In[60]:

print "program started"
s=raw_input("Enter sequence to iterate: ")
for i in s:
    print "iteration started"
    if i== " ":
        continue
    print i
    print "iteration ended"
print "other statements in program"
print "program ended"


# In[61]:

print "program started"
s=raw_input("Enter sequence to iterate: ")
for i in s:
    print "iteration started"
    print i
    print "iteration ended"
print "other statements in program"
print "program ended"


# In[62]:

for i in "python program":
    continue
print i


# In[63]:

for i in "python program":
    break
print i


# In[64]:

i=0
while i<10:
    i=i+1
    break
print i


# In[65]:

i=0
while i<10:
    i=i+1
    continue
print i


# In[66]:

"abc".isupper()


# In[67]:

"Abc".isupper()


# In[68]:

"ABC".isupper()


# In[69]:

"123ABC".isupper()


# In[70]:

"123Abca".isupper()


# In[71]:

"123".isupper()


# In[72]:

"".isupper()


# In[73]:

"#$%".isupper()


# In[74]:

"#$%ABC".isupper()


# In[75]:

s=raw_input("enter a string: ")
for char in s:
    if char.isupper():
        print "given string contains capital letters"
        break
        


# In[76]:

s="python program"


# In[77]:

s.capitalize()


# In[78]:

s="pyTHONn proGRAM"
print s.capitalize()


# In[79]:

s


# In[80]:

s="python program"
print s.find("pyt")


# In[81]:

s="python program"
print s.find("gram")


# In[82]:

s="python program"
print s.find("java")


# In[83]:

s.find("PYTHON")


# In[85]:

s="python program"
sub = "PytHon"

s_l = s.lower()
sub_l = sub.lower()
print s_l.find(sub_l)
print s_l
print sub_l


# In[86]:

s


# In[87]:

s.find('p')


# In[88]:

get_ipython().magic(u'pinfo s.find')


# In[89]:

s.find('p',3)


# In[ ]:



