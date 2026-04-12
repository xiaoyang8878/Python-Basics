string = 'Hello 1牛3 Python'

"""
正向索引和反向索引都可以使用
步长默认为1, 取连续的数据
"""
print(string[7: 11])  # '牛3 P'
print(string[-9: -5])  # '牛3 P'
print(string[7: -5])  # '牛3 P'
print(string[-9: 11])  # '牛3 P'

""" 步长为2, 取数据时要隔一个再取 """
print(string[7: 14: 2])  # '牛 yh'

""" 步长为3, 取数据时要隔两个再取 """
print(string[7: 14: 3])  # '牛Ph'

""" 步长为负数, 表示从右往左取数据 """
print(string[10: 6: -1])  # 'P 3牛'

""" 步长为-2, 表示从右往左隔一个取数据 """
print(string[13: 6: -2])  # 'hy 牛'

""" 步长为正数, start没有指定, 默认为0 """
print(string[: 3])  # 'Hel'
print(string[0: 3])

""" 步长为负数, start没有指定, 默认为-1 """
print(string[: 12: -1])  # 'noh'
print(string[-1: 12: -1])

""" 步长为正数, end没有指定, 默认为len(string) """
print(string[13:])  # 'hon'
print(string[13:len(string)])

""" 步长为负数, end没有指定, 默认为-len(string)-1 """
print(string[2::-1])  # 'leH'
print(string[2:-len(string)-1:-1])

""" 把该序列复制一份 """
print(string[:])

""" 把该序列倒过来 """
print(string[::-1])

""" start到end是从左往右，但step表示从右往左 """
print(string[1: 3: -1])  # ''



""" 类比0维数据 """
item1 = 1
item2 = 2
item3 = 3
item4 = 4
item5 = 5
item6 = 6
item7 = 7
item8 = 8
item9 = 9

""" 类比1维数据 """
lst1 = [item1, item2, item3]
lst2 = [item4, item5, item6]
lst3 = [item7, item8, item9]
# 对1维数据索引，结果为0维数据
print(lst1[0])  # 1
print(lst2[1])  # 5
print(lst3[2])  # 9
# 无论怎么切片，维度保持不变
print(lst1[::2])  # [1, 3]
print(lst2[1:2])  # [5]
print(lst3[::2][1:2])  # [9]

""" 类比2维数据 """
lst4 = [lst1, lst2, lst3]
# 对2维数据索引，结果为1维数据
print(lst4[0])  # [1, 2, 3]
print(lst4[1])  # [4, 5, 6]
print(lst4[2])  # [7, 8, 9]
# 并且每索引一次，降低一次维度
print(lst4[0][1])  # 2
# 无论怎么切片，维度保持不变
print(lst4[::2])  # [[1, 2, 3], [7, 8, 9]]
print(lst4[1:2])  # [[4, 5, 6]]
print(lst4[::2][1:2])  # [[7, 8, 9]]