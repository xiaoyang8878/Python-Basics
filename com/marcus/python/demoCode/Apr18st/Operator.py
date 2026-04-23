a = 5
b = 2
print(a + b)  # 7
print(a - b)  # 3
print(a * b)  # 10
print(a / b)  # 2.5
print(a ** b)  # 25
print(a // b)  # 2
print(a % b)  # 1
print(-15 % 4)  # 1 --> -15-4*-4
# print(-15-4*-4)

a = 456
b = 456
c = 789
print(a == b)
print(a != c)
print(c > a)
print(b < c)
print(a >= b)
print(a <= b)

a = 3

c = a + 2
print(c)  # 5

c += a
print(c)  # 8   结果等于 c = c + a

c -= a
print(c)  # 5   结果等于 c = c - a

c *= a
print(c)  # 15   结果等于 c = c * a

c /= a
print(c)  # 5.0   结果等于 c = c / a

c %= a
print(c)  # 2.0   结果等于 c = c % a

c **= a
print(c)  # 8.0   结果等于 c = c ** a

c //= a
print(c)  # 2.0   结果等于 c = c // a

lst1 = [1, 2]
lst2 = [3, 4, 5]
print(id(lst1))
lst1 += lst2
print(id(lst1))
print(lst1)


lst1 = [1, 2]
lst2 = [3, 4, 5]
print(id(lst1))
lst1 = lst1 + lst2
print(id(lst1))
print(lst1)

a = [1, 2, 3, 4]
b = [4, 3, 2, 1]
c = a
print(id(a))
print(id(b))
print(id(c))


"""

**+、* 的拼接操作**
    - +、+=、*、\\*= 还支持字符串、列表、元组的拼接操作

"""
str1 = 'hello '
str2 = 'world'
print(str1 + str2)  # hello world
str1 += str2    # hello world
print(str1)

str1 = 'hello '
print(str1 * 3)  # hello hello hello
str1 *= 3
print(str1)  # hello hello hello


lst1 = [1, 2]
lst2 = [3, 4, 5]
print(lst1 + lst2)  # [1, 2, 3, 4, 5]
lst1 += lst2
print(lst1)  # [1, 2, 3, 4, 5]

lst1 = [1, 2]
print(lst1 * 3)  # [1, 2, 1, 2, 1, 2]
lst1 *= 3
print(lst1)  # [1, 2, 1, 2, 1, 2]


tup1 = (1, 2)
tup2 = (3, 4, 5)
print(tup1 + tup2)  # [1, 2, 3, 4, 5]
tup1 += tup2
print(tup1)  # [1, 2, 3, 4, 5]

tup1 = (1, 2)
print(tup1 * 3)  # [1, 2, 1, 2, 1, 2]
tup1 *= 3
print(tup1)  # [1, 2, 1, 2, 1, 2]

"""
基本序列赋值
    - 格式： a, b, c, ... = iterable
    - 将iterable的元素分别赋值给对应变量，元素和变量个数需要一致
"""
a, b = 3, 4
print(a, b)

a, b, c = [3, 4, 5]
print(a, b, c)

a, b, c, d = '你好吗?'
print(a, b, c, d)

"""
多目标赋值
    - 将一个对象同时赋值给多个变量。
"""
a = b = c = 999
print(id(a))
print(id(b))
print(id(c))


a = b = c = [1, 2, 3]
print(id(a))
print(id(b))
print(id(c))

b.append(4)
print(a)
print(b)
print(c)

print("---------------------------------------------------------------------------------------------------------------")
"""
逻辑运算符

| 运算符  | 描述                                                     |
| ------ | -------------------------------------------------------- |
| and    | 布尔"与"（左边bool判定为False，返回左边；否则返回右边）  |
| or     | 布尔"或"（左边bool判定为True，返回左边；否则返回右边）   |
| not    | 布尔"非"（判定为False，返回True；判定为True，返回False） |
"""
a = 2
b = 'hello'
c = []
d = 0

print(c and a)  # []        c -> false 左边为false 返回左边
print(a and c)  # []        a -> true  左边为true 返回右边
print(d and c)  # 0         d -> false 返回左边d
print(c and d)  # []        c -> false 返回左边c
print(a and b)  # 'hello'   a -> true 返回右边b -> hello
print(b and a)  # 2         b -> true 返回右边a -> 2

print(a or c)  # 2          a -> true 返回左边 a -> 2
print(c or a)  # 2          c -> false 返回右边 a -> 2
print(b or a)  # 'hello'    b -> true 返回左边b -> hello
print(a or b)  # 2          a -> true 返回左边 a -> 2
print(c or d)  # 0          c -> false 返回右边 d -> 0
print(d or c)  # []         d -> false 返回右边 c -> []

print(not a)  # False       a -> true --> not a = false
print(not b)  # False       b -> true --> not b = false
print(not c)  # True        c -> false --> not c = true
print(not d)  # True        d -> false --> not d = true
#
# # 优先级：not > and > or
print(b and not a or c)  # []    not a --> false -> b and false = false --> false or c -> c -> []
print("---------------------------------------------------------------------------------------------------------------")

'''
短路机制
    - 在逻辑表达式中，由于and和or的特点，表达式中的部分内容可能不会执行
'''
a = 0
b = 1
c = ()

print(c and b / c)  # ()    c -> false 返回c，并未执行b/c -->()
print(b or a + c)  # 1      b -> true 返回b，并未执行a + c --> 1
# b and a + c  # Error

s = 'hello'

print(s == 'hello' or s == 'hello')

print('---------------------------------------------------------------------------------------------------------------')


'''
all(iterable)
    - 如果 iterable 的所有元素 bool 判定都为 True，则返回 True
    
any(iterable)
    - 如果 iterable 中存在至少一个元素 bool 判定为 True，则返回 True
'''
tup = ('0', ' ', 'None', 'False', '[]')
print(all(tup))  # True

tup = (0, ' ', 'None', 'False', '[]')
print(all(tup))  # False

tup = (0, '', None, False, [])
print(any(tup))  # False

tup = ('0', '', None, False, [])
print(any(tup))  # True
print('---------------------------------------------------------------------------------------------------------------')


'''
in and not in
'''
string = 'hello world'
print('e' in string)  # True
print('lo' in string)  # True
print('ol' not in string)  # True

lst = [5, 6, [2, 3], 4]
print(6 in lst)  # True
print(2 not in lst)  # True
print(3 not in lst)  # True
print([5, 6] not in lst)  # True
print([2, 3] in lst)  # True

d = {2: 3, 4: 5}
print(2 in d)  # True
print(3 not in d)  # True
print('---------------------------------------------------------------------------------------------------------------')


'''
a is b --> id(a) == id(b)
a is not b --> id(a) != id(b)
'''
a = [257]
b = [257]
print(a == b)  # True
print(a is b)  # False
print(id(a) == id(b))  # False

a = [257]
b = a
print(a == b)  # True
print(a is b)  # True
print(id(a) == id(b))  # True


'''
## 运算符优先级

以下表格优先级从高到低优：

| 运算符                        | 描述                    |
| ---------------------------- | ---------------------- |
| **                           | 指数                    |
| \*  /  %  //                 | 乘，除，求余数和取整除      |
| \+  -                        | 加法、减法               |
| <=  <  >  >=                 | 比较运算符               |
| ==   !=                      | 比较运算符               |
| %=  /=  //=  -=  +=  *=  **= | 增强赋值                 |
| is     is not                | 身份运算符                |
| in     not in                | 成员运算符                |
| not  and  or                 | 逻辑运算符                |
| =                            | 简单赋值                  |
'''