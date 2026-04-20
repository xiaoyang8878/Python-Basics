"""
range(statr, stop, step)
创建一个range类型的数据并返回，
该数据是一个等差的整数序列，是不可变的，是iterable

只传两个参数的时候，step默认为1
只传一个参数的时候，参数赋值为stop，start默认为0，step默认为1
"""

r = range(1, 10, 2)
# # print(r)
# # print(type(r))
# # print(len(r))
# # print(r[3])
# # print(r[::2])
#
# print(list(r))
# print(tuple(r))

# for i in r:
#     print(i)
#
# print('---------------------------------------------------------------------------------------------------------------')
# r = range(9, 0, -2)
# print(list(r))
#
# r = range(4, 8)
# print(list(r))
#
# r = range(8)
# print(list(r))

# lst = ['d', 'c', 'k', 'a']
# for i in lst:
#     print(lst.index(i), i)
# for i in lst:
#     print(lst.index(i), i)

# for i in range(len(lst)):
#     print(i, lst[i])

"""
enumerate(iterable, start=0)
创建一个enumerate类型的数据并返回,
返回值为迭代器对象
"""

# en = enumerate('ASDF')
# print(en, type(en))
# for e in en:
#     print(e)

# while next(en):
#     print(next(en))

# total = 0
# lst = [3543.2, 198.65, 1452.2, 942.54, 300.52, 9250]
# for item in lst:
#     total += item
# print(total)

"""
列表推导式
语法
    [exp for子句]
    [exp for子句 更多的for子句或if子句]
类比
lst = []
for i in range(1, 9, 2):
    lst.append(i ** 2)

"""
# lst = [i ** 2 for i in range(1, 9, 2)]
# print(lst)
# lst = []
# for i in range(1, 9, 2):
#     lst.append(i ** 2)
# print(lst)


lst = [i + j for i in range(1, 9, 2) for j in range(4) if j % 2]
'''
lst = []
for i in range(1, 9, 2):
    for j in range(4):
        if j % 2:
           lst.append(i + j) 
'''
print(lst)
