"""
基本数据类型
    数字(Number)
        - 特性：不可变，不是序列
        - 分类：整数、浮点数、布尔型、复数
    整数（int）：
        - 包括正整数，负整数和零，如：798，-789，0
    浮点数（float）：
        - 和数学中的小数类似，如：3.14
        - 科学计数法认定为浮点数，如：3e4,3E4
    布尔型（bool）：
        - 布尔型只有两个值，分别是关键字True和False，它们被当成数字是，大小分别为1和0
    复数（complex）：
        - 实部+虚部，表示为a+bj或a+bJ，例如：3+4j，3+4J
"""

"""
type(obj)
    返回obj的数据类型
"""
print("------ type(obj) -------")
num1 = 789
num2 = 789.789
num3 = True
num4 = 3+4j
string = 'hello'
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
print(type(string))

"""
int([x])
    - x: 接受数字或特定字符串
    - 将x转换为整数并返回，如果没有给x指定值，则返回0
"""
print("------- int([x]) -------")
print(int()) #0
print(int(3)) #3
print(int(-3)) #-3
print(int(0)) #0
print(int(3.14)) #3
print(int(3.99)) #3
print(int(0.0)) #0
print(int(True)) #1
print(int(False)) #0
print(int('12')) #12
print(int('-12')) #-12

"""
float([x])
    - x：接收数字或特定字符串
    - 将x转换为浮点数并返回，如果没有给x指定值，则返回0.0
"""
print("------- float() -------")
print(float()) #0.0
print(float(3)) #3.0
print(float(-3)) #-3.0
print(float(0)) #0.0
print(float(3.99)) #3.99
print(float(-3.99)) #-3.99
print(float(0.0)) #0.0
print(float(True)) #1.0
print(float(False)) #0.0
print(float('12')) #12.0
print(float('-12')) #-12.0
print(float('12.1')) #12.1

"""
bool([x])
    - 根据x指定得值，返回布尔值
    - 如果没有给x指定值，则返回False
    - 数字0, 0.0, 0j, False,
    - 空字符串, 空列表, 空元组,空字典, 空集合, None, ...
    - 以上这些数据bool判定为False,
    - 其它数据通常判定为True
"""
print("------- bool() -------")
print(bool()) #Flase
print(bool(0)) #Flase
print(bool(0.0)) #Flase
print(bool(0j)) #Flase
print(bool(False)) #Flase
print(bool('')) #Flase
print(bool([])) #Flase
print(bool(())) #Flase
print(bool({})) #Flase
print(bool(set())) #Flase
print(bool(None)) #Flase
print(bool('0'))  # True
print(bool(' '))  # True
print(bool('None'))  # True
print(bool('False'))  # True
print(bool('[]'))  # True

"""
complex(real=0, imag=0)
    - 创建一个 real + imag*1j 的复数并返回
    - 如果第一个参数是字符串，它将被解释为复数，此时不能传第二个参数
    - 如果没有传实参，则返回0j
"""
print("------- complex() -------")
print(complex())  # 0j
print(complex(3.2, 4))  # (3.2+4j)
print(complex(3.2))  # (3.2+0j)
print(complex('3.2'))  # (3.2+0j)
print(complex("3.2+4j"))  # (3.2+4j)