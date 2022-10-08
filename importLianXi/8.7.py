import __init__
from __init__ import jiafa
from __init__ import jiafa as jia
import __init__ as han
from hanshu import *

c=__init__.jiafa(5,6) # 第一个导入对应的调用
d=jiafa(5,6)        # 第二个导入对应的调用
e=jia(5,6)          # 第三个导入对应的调用
f=han.jiafa(5,6)    # 第四个导入对应的调用

print(c,d,e,f)
