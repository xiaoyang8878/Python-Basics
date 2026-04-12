"""
字典的元素是以键值对(key: valut)的形式存在的，是一种映射结构
字典不是序列
字典是可变的
字典的键是不能存在可变数据，值没有限制
    dic = {'name': 'John', 'age': 25, 'height': 70, [1, 2]: 86}
字典的键会自动去重（保留第一个重复项），对应的值做更新；值可以重复
当字典作为一个iterable进行操作时，只有键参与迭代，值不参与
"""

# dic = {'name': 'John', 'age': 25, 'height': 70, 'weight': 86}
# print(dic['name'])
# print(len(dic))

'''
dict.keys()
    - 返回由字典所有键组成的一个新视图
    - 返回的对象是视图对象，这意味着当原字典改变时，视图也会相应改变
'''
d = {'name': 'Tom', 'age': 15, 'height': 162}
view_keys = d.keys()  # dict_keys(['name', 'age', 'height'])
print(view_keys)

# # 修改字典
d['weight'] = 59

print(view_keys)

'''
dict.values()
    - 返回由字典所有值组成的一个新视图
    - 返回的对象是视图对象，这意味着当字典改变时，视图也会相应改变
'''
view_values = d.values()
print(view_values)  # dict_values(['Tom', 15, 162, 59])

# 修改字典
d['weight'] = 75
print(view_values)

'''
dict.items()
    - 返回由字典所有键和值组成的一个新视图
    - 返回的对象是视图对象，这意味着当字典改变时，视图也会相应改变
'''

view_items = d.items()
print(view_items)

# 修改字典
d['weight'] = 59

print(view_items)   # dict_items([('name', 'Tom'), ('age', 15), ('height', 162), ('weight', 75)])


"""
dict_keys
dict_values
dict_items
是字典的视图对象
"""

'''
dict.get(key, default=None)
    - key：键
    - default：如果指定的键不存在时，返回该值，默认为 None
    - 返回指定的键对应的值，如果 key 不在字典中，则返回 default
'''
d = {'name': 'Tom', 'age': 15, 'height': 162}
print(d.get('age'))
print(d.get('weight'))
print(d.get('weight', '该键不存在'))

print('-----------------------------------------------------------------------------------------------')
'''
dict.update([other])
    - 用 other 来更新原字典，没有返回值
    - other 可以像 dict() 那样传参
'''
d = {'name': 'Tom', 'age': 15, 'height': 162}
# d.update(age=18, weight=59)
# d.update({'age': 18, 'weight': 59})

# print(zip(['age', 'weight'], [18, 59]))

'''
zip(*iterables, strict=False)
    并行迭代多个可迭代对象，生成一个由每个对象中的一个元素组成的元组。
    Create and return a new object.  See help(type) for accurate signature.

    *iterables
        不定长参数
        可以接收[0,+∞)个参数，贪婪的，将它们打包成一个元组，如果没有接收到，则为空元组
    
    
dict():
    dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    # (copied from class doc)
    
    **kwargs
        可以接收[0,+∞)个参数，贪婪的，将它们打包成一个字典，如果没有接收到，则为空字典
        
'''
# lst = [1, 2, 3, 4, 5]
# str = 'Hello'
#
# for item in zip(lst, str):
#     print(item)

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
listZipped = list(zipped)
print(listZipped)  # [(1, 4), (2, 5), (3, 6)]
x2, y2 = zip(*listZipped)  # 解压还原操作
print(x == list(x2) and y == list(y2))  # True
print(x2)
print(y2)

# d.update(zip(['age', 'weight'], [18, 59]))
# # d.update([('age', 18), ('weight', 59)])
# print(d)

