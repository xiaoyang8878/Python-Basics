"""
在Python 中，关键字是一组预定义的标识符，他们具有特定的语法功能和用途，
这些关键字在python的语法中扮演着至关重要的角色。
例如：
    def: 用于定义函数
    class: 用于定义类
    if: 用于条件语句
"""

"""
在python中，不管是函数还是类的定义，与Java有所不同，Java中是用花括号{}包着函数体或者类的内容
python使用的是冒号 : 以及缩进来表示函数体或者类的内容，缩进表示层级关系，所以在编写python的时候需要注意缩进
"""
def functionName(arg1, arg2):
    return arg1 + arg2

class Student(object):
    age = 31
    name = "包包"

c = 2
if c >0 :
    print(8 / c) # 只要是做除法运算，结果都为浮点型