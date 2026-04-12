"""
列表 - List
    - 特性：可变，是序列
    - 列表用方括号定义，元素没有类型限制
"""

lst1 = []
lst2 = [567]
lst3 = [567, 'hello', 3 + 4j, lst2]
print(lst2)
print(lst3)

'''
修改列表
    列表是可变的，可以通过索引和切片的方式来对列表的元素重新赋值
'''
lst = [567, 'Hello', 78.9, 'World', False]

"""
针对一个元素：
格式: lst[index] = object 
"""
lst[0] = 7654
lst[3] = 'World~'
print(f"lst: {lst}")

"""
针对多个元素(切片赋值):
格式:  lst[start: end: step] = iterable
注意：
    - 边界规则： 
        核心规则 -- 左闭右开区间 [start, end)
    - 切片赋值不等长替换逻辑
        先删除切片范围内的元素，再插入右边列表的所有元素
    - step：步长就是跳几步，正向左来负向右
                            快速参考表
            需求              代码            示例(lst=[0,1,2,3,4,5])
            --------------------------------------------------------------
            所有元素          lst[:]	        [0,1,2,3,4,5]
            反转             lst[::-1]	    [5,4,3,2,1,0]
            偶数索引	        lst[::2]	    [0,2,4]
            奇数索引	        lst[1::2]	    [1,3,5]
            每3个取1个        lst[::3]	    [0,3]
            从索引2开始每2个   lst[2::2]	    [2,4]
            反向每隔1个	    lst[::-2]	    [5,3,1]
            最后3个	        lst[-3:]	    [3,4,5]
            去掉首尾	        lst[1:-1]	    [1,2,3,4]
"""
lst[2:3] = [89.9]  # 只修改index = 2 的元素
print(lst)
lst[2:4] = [99.9, 'World~~', True]  # 修改index = 2，3的两个元素，使用切片赋值不等长替换逻辑，先删除2 3 两个元素，再插入三个元素
print(lst)

lst[2:3] = [7, 8, 9]  # 修改index=2的元素，先删除index=2的元素值，再插入右边三个元素
print(lst)  # [7654, 'Hello', 7, 8, 9, 'World~~', True, False]

lst[2:4] = [1, 2, 3]  # [7654, 'Hello', 1, 2, 3, 9, 'World~~', True, False]
print(lst)
lst[1:4] = [1, 2]  # [7654, 1, 2, 3, 9, 'World~~', True, False]
print(lst)

lst[2:3] = []  # 删除index=2的元素
print(lst)  # [7654, 1, 3, 9, 'World~~', True, False]

lst[1:4] = []  # 删除index=1 2 3的元素
print(lst)  # [7654, 'World~~', True, False]

# step不为1, 只能 n vs n
lst[1::2] = ['a', 'b']  # 从index =1 开始， 步长为2，因为没有指定stop，是从左到右取奇数索引
print(lst)  # [7654, 'World~~', True, False] --> [7654, 'a', True, 'b']
"""
 但是如果上面代码修改为 lst[1::2] = ['a', 'b', 'c']，就会报错，因为当step不为1时，切片赋值两边元素数量要相等
"""
# print(lst)

"""
Traceback (most recent call last):
    lst[1::2] = ['a', 'b', 'c']
    ~~~^^^^^^
ValueError: attempt to assign sequence of size 3 to extended slice of size 2
"""

'''
当 start = stop = n时，表示空切片，逻辑为在index = n 前面插入元素
'''
lst[0:0] = ['a']  # 在index = 0 前面插入元素
print(lst)  # [7654, 'a', True, 'b'] --> ['a', 7654, 'a', True, 'b']
lst[1:1] = ['b']  # 在index = 1 前面插入元素
print(lst)  # ['a', 'b', 7654, 'a', True, 'b']
lst[len(lst):] = ['c']  # 在列表的最后插入一个元素
print(lst)  # ['a', 'b', 7654, 'a', True, 'b', 'c']

# 插入多个元素
lst[0:0] = ['a', 'b', 'c']  # 在列表开头插入三个元素
print(lst)  # ['a', 'b', 'c', 'a', 'b', 7654, 'a', True, 'b', 'c']
lst[1:1] = ['d', 'f']  # 在index = 1的位置前插入两个元素
print(lst)  # ['a', 'd', 'f', 'b', 'c', 'a', 'b', 7654, 'a', True, 'b', 'c']
lst[len(lst):] = ['x', 'y', 'z']  # 在最后插入三个元素
print(lst)  # ['a', 'd', 'f', 'b', 'c', 'a', 'b', 7654, 'a', True, 'b', 'c', 'x', 'y', 'z']

print('---------------------------------------------------------------------------------------------------------------')

"""
list([iterable])
    - 将一个iterable对象转化为列表并返回，如果没有传实参，则返回空列表
"""
print(list())
print(list("hello"))  # ['h', 'e', 'l', 'l', 'o']
print(list((1, 2, 3)))

# 字典作为一个iterable, 只有键参与迭代
print(list({1: 2, 3: 4}))
print(list({'a', 'b', 'c', 789, 456}))  # {'a', 'b', 'c', 789, 456} 表示为无序集合

print('---------------------------------------------------------------------------------------------------------------')
"""
列表方法
    list.append(object)
        - 往列表中追加一个元素，无返回值，相当于 lst[len(lst):] = [object]
        
    list.extend(iterable)
        - 使用 iterable 中的所有元素来扩展列表，无返回值，相当于 lst[len(lst):] = iterable
        
    list.insert(index, object)
        - index：要插入元素的位置
        - object：要插入的元素
        - 在指定位置插入一个元素，无返回值
        
    list.sort([key], reverse=False)
        - key：必须指定一个可调用对象（比如：函数，类）
        - reverse：默认为False，代表升序，指定为True，则为降序
        - 对原列表进行排序，无返回值
        
    sorted(iterable, [key], reverse=False)
        - iterable：要排序的可迭代对象
        - key：指定一个函数，在排序之前，每个元素都先应用这个函数之后再排序
        - reverse：默认为 False，代表升序，指定为 True 则为降序
        - 对可迭代对象进行排序，以列表形式返回排序之后的结果
        
    list.reverse()
        - 把列表中的元素倒过来，无返回值
        
    list.count(x)
        - 返回元素 x 在列表中出现的次数
        
    list.index(x[, start[, end]])
        - x：要找的值
        - start：起始索引，默认为 0
        - end：结束索引（开区间），默认为 len(lst)
        - 返回从左边开始第一次找到指定值时的正向索引，找不到报错
        
    list.pop(i=-1)
        - i：要删除并返回的元素的索引
        - 删除列表中指定索引的元素并返回该元素，默认最后一个
        - 索引超出范围，则报错
        
    list.remove(x)
        - 删除列表中从左往右遇到的第一个x元素，无返回值
        - 如果没有这样的元素，则报错
        
    list.copy()
        - 返回该列表的一个副本，等价于 lst[:]
        
    list.clear()
        - 移除列表中的所有元素，无返回值，等价于 del lst[:]
        
  *** Python中的删除操作通常不是直接删除内存中的数据，而是解除引用关系，当数据的引用计数为0时，该数据就变为了一个可回收的对象，然后会被Python自动回收。 ***

"""


#  list.append(object)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)
lst.append(11)
print(f'list.append(object): {lst}')

#  list.extend(iterable)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst.extend([11, 12, 13, 14, 15])
print(f'list.extend(iterable): {lst}')

#  list.insert(index, object)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst.insert(0, ['a', 'b'])
print(f'list.insert(index, object): {lst}')

#  list.sort([key], reverse=False)
lst = [1, 2, -6, 9, 8, -9, 3, 10]
lst.sort()
print(f'list.sort(): {lst}')
lst.sort(reverse=True)
print(f'list.sort(reverse=True): {lst}')

# chr(i) 返回Unicode码位为指定整数的字符
# ord(c) 返回指定字符对应的Unicode码位
print(chr(97))  # 'a'
print(ord('a'))  # 97

# 字符串在大小比较时是逐个字符进行比较的
# 根据字符在编码表里的位置
lst = ['10', '2', '1', '-3', '101']
lst.sort()
print(lst)

# abs(number) 内置函数，返回number的绝对值
print(abs(9))  # 9
print(abs(9.87))  # 9.87
print(abs(0))  # 0
print(abs(-9))  # 9
print(abs(-9.87))  # 9.87
print(abs(True))  # 1
print(abs(False))  # 0
print(abs(3+4j))  # 求模, 5.0


"""
对lst中的元素按照绝对值的大小降序排序

把lst中的每个元素依次作为实参传递给key所指定的函数去调用, 即:
abs(1), abs(2), abs(-5), abs(-3)
返回值分别为: 1, 2, 5, 3
根据返回值的大小对原数据进行排序
"""
lst = [1, 2, -5, -3]
lst.sort(key=abs, reverse=True)
print(lst)

"""
对lst中的元素按照数字的大小升序排序

把lst中的每个元素依次作为实参传递给key所指定的类去调用, 即:
int('10'), int('2'), int('1'), int('-3'), int('101')
返回值分别为: 10, 2, 1, -3, 101
根据返回值的大小对原数据进行排序
"""
lst = ['10', '2', '1', '-3', '101']
lst.sort(key=int)
print(lst)

# sorted(iterable, [key], reverse=False)
lst = [1, 2, -5, -3]

# 升序排序
print(sorted(lst))

# 降序排序
print(sorted(lst, reverse=True))

# 对lst中的元素按照绝对值的大小降序排序
print(sorted(lst, key=abs, reverse=True))

'''
对字符串排序

print(ord('h'))  # 104
print(ord('e'))  # 101
print(ord('l'))  # 108
print(ord('o'))  # 111
print(ord(' '))  # 32
print(ord('w'))  # 119
print(ord('r'))  # 114
print(ord('d'))  # 100
'''
print(sorted('hello world'))  # [' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']

'''
list.reverse() 

方法          	是否创建副本          	是否修改原列表         	返回值	            适用场景
--------------------------------------------------------------------------------------------------
lst[::-1]	        ✅ 是	                ❌ 否	            新列表	            需要保留原列表
list(reversed(lst))	✅ 是	                ❌ 否	            新列表	            需要保留原列表，可读性好
reversed(lst)	    ❌ 否	                ❌ 否	            迭代器	            只需遍历一次，节省内存
lst.reverse()	    ❌ 否	                ✅ 是	            None	            不需要原列表，性能最高

'''
lst = [1, 3, 5, 2]
lst.reverse()  # inplace 原地修改
print(lst)

lst = [1, 3, 5, 2]
print(lst[::-1])  # copy

lst = [1, 3, 5, 2]
print(list(reversed(lst)))

lst = [1, 3, 5, 2]
print(reversed(lst))


# list.count(x)
lst = [1, 3, 2, '23', [2, 4]]
print(lst.count(2))  # 1

# list.index(x[, start[, end]])
lst = [1, 2, 3, 2, '23', [2, 4]]
print(lst.index(2))  # 1

# lst.index(4)  # Error 4 is not in list

# list.pop(i=-1)
lst = [567, 'hello', True, False, 456]
print(lst.pop(1))  # 'hello'
print(lst)  # [567, True, False, 456]

# list.remove(x)
lst = [1, 2, 4, 2, 3, 3]
print(lst.remove(2))
lst.remove(2)
print(lst)

# list.copy()
lst = [567, 'hello', True, False, 456]
new_lst = lst.copy()
print(new_lst)

# list.clear()
lst = [567, 'hello', True, False, 456]
lst.clear()
# del lst[:]
print(lst)  # []

print('---------------------------------------------------------------------------------------------------------------')

# Python中的删除操作通常不是直接删除内存中的数据，而是解除引用关系，当数据的引用计数为0时，该数据就变为了一个可回收的对象，然后会被Python自动回收。
lst1 = [567, 'hello', 456, [912, 923], 'world']
lst2 = lst1

del lst1
print(lst2)  # [567, 'hello', 456, [912, 923], 'world']

del lst2[1]
print(lst2)  # [567, 456, [912, 923], 'world']

del lst2[0], lst2[2]
print(lst2)  # # [456, [912, 923]]

del lst2[:3:2]
print(lst2)  # [[912, 923]]

# del lst2[3][0]  # list index out of range
# print(lst2)

# del lst2[0][1]
# print(lst2)

del lst2[:]
print(lst2)  # []



lst =  [567, 'hello', 456, [912, 923]]
lst.append(lst)


a = "hello"
b = ["hello", "world"]
c = 3 + 4j
tup = (a, b, c)
print(tup)
a = 121
print(tup)
print(a)