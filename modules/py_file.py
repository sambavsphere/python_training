'''
import f1
import module1
'''
'''
from module1 import file1
print file1.fun1()

'''
'''
import module1

print module1.file1.fun1()
'''
'''
import module1
print module1.file1.fun1()
'''
'''
from module1 import file1,file2
print file1.fun1()
print file2.fun2()
'''
'''

import module1	
print module1.file1.fun1()
print module1.file2.fun2()
'''
'''
from module1.inside import file3
'''
'''
from module1 import inside
print inside.file3.fun()
'''

from module1.inside import file3
print file3.fun()