""" 
请用户输入身高(m)和体重(kg), 并根据BMI公式(体重/身高的平方)计算出的BMI指数来判断用户的体重情况
判断标准：
BMI >= 35 为重度肥胖
30 <= BMI < 35 为中度肥胖
27 <= BMI < 30 为轻度肥胖
23 <= BMI < 27 为超重
18.5 <= BMI < 23 为正常体重
BMI < 18.5 为轻体重
"""

strHeight = input("请输入您的身高(m): ")
strWeight = input("请输入您的体重(kg): ")
bmi = round(float(strWeight) / float(strHeight) ** 2, 2)

category = ''

if bmi >= 35:
    category = '重度肥胖'
elif 30 <= bmi <= 35:
    category = '中度肥胖'
elif 27 <= bmi < 30:
    category = '轻度肥胖'
elif 23 <= bmi < 27:
    category = '超重'
elif 18.5 <= bmi < 23:
    category = '正常体重'
elif bmi < 18.5:
    category = '轻体重'

print(f'您的身高为: {strHeight}m')
print(f'您的体重为: {strWeight}kg')
print(f'您的BMI指数为: {bmi}')
print(f'体重情况为: {category}')

"""
实现程序：请用户输入一个正整数 n, 程序计算并输出该整数「各位数字之积」与「各位数字之和」的差

示例:
输入: n = 234
输出: 15 

解释:
各位数之积 = 2 * 3 * 4 = 24 
各位数之和 = 2 + 3 + 4 = 9 
结果 = 24 - 9 = 15
"""

num = input('请输入一个正整数: ')
product = 1
total = 0

for char in num:
    total += int(char)
    product *= int(char)

result = product - total
print(result)

"""
已知字典 d = {'a': 100, (): '9', 8.1: 'b', True: 3+4j}, 计算键和值中所有数字类型的数据之和

即: 100 + 8.1 + True + 3+4j = (112.1+4j)
"""

numType = [int, float, complex, bool]

d = {'a': 100, (): '9', 8.1: 'b', True: 3 + 4j}

total = 0

for key, value in d.items():
    if type(key) in numType:
        total += key
    if type(value) in numType:
        total += value

print(total)

"""
定义函数实现: 对于一个任意的正整数, 判断其是否为阿姆斯特朗数。

如果一个n位正整数等于其各位数字的n次方之和, 则称该数为阿姆斯特朗数。 例如1**3 + 5**3 + 3**3 = 153。

1000以内的阿姆斯特朗数:  1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
"""


def is_narcissistic_number(num):

    str_num = str(num)

    len_num = len(str_num)

    total_num = 0

    for i in str_num:
        total_num += int(i) ** len_num

    return total_num == int(num)


test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 88, 91, 50, 153, 370, 371, 407]

for num in test_numbers:
    print(f'{num}: {is_narcissistic_number(num)}')