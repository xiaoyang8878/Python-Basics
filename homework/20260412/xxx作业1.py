# string = 'hello world', 如何切片可以得到 'hello w'?
str = 'hello world'

print(str[:str.find('w')+1])


# string = 'hello world', 如何切片(不是索引)可以得到空格字符?

print(str[str.find(' '):str.find(' ')+1])

# string = 'hello world', 如何切片可以得到 'doo'?

indexEnd = str.find('o')  # 找出第一个o字符的index
print(str[:indexEnd - 1:-3])  # indexEnd是开区间，step为-3，从右往左数，所以indexEnd 要-1



# 给定时间字符串 t = "2025/10/28-14:35:48"，提取月份和分钟数并计算它们的乘积

t = "2025/10/28-14:35:48"
'''
1. 用split 将字符串切成['2025', '10', '28-14:35:48']
2. 将 2025 转成float
3. 用split 将'28-14:35:48'切割成['28-14', '35', '48']
'''
tSplit = t.split('/')

month = float(tSplit[1])
min = float(tSplit[2].split(':')[1])
result = month * min
print(result)




# 给定字符串 s = "12a3a4AA5A"，求出'A'字符和'a'字符的数量差

s = "12a3a4AA5A"
result = s.count('A') - s.count('a')
print(result)

"""
编写一个程序, 帮助水果店实现计价功能:
请用户输入水果品种, 水果单价(元/kg)和重量(kg),
计算出需要花费的金额并做格式化输出

例:
用户输入水果品种为: 苹果
输入单价为: 3.98
输入重量为: 2.58
根据用户输入数据计算出总价为: 10.2684

请用三种字符串格式化方式输出如下结果:
您购买了2.58kg的苹果, 单价为3.98元/kg, 您需要支付10.27元!
"""

fruit = input('欢迎来到xxx水果店！\n请输入您需要购买的水果品种： ')
price = float(input('请输入单价：'))
weight = float(input('请输入重量：'))
totalPrice = price * weight
# %格式化
print('您购买了%.2fkg的%s, 单价为%.2f元/kg, 您需要支付%.4f元!' % (weight, fruit, price, totalPrice))
# format格式化
print('您购买了{:.2f}kg的{}, 单价为{:.2f}元/kg, 您需要支付{:.4f}元!'.format(weight, fruit, price, totalPrice))
# f-string格式化
print(f'您购买了{weight:.2f}kg的{fruit}, 单价为{price:.2f}元/kg, 您需要支付{totalPrice:.4f}元!')



# 已知 lst = [1, 3, 2, 6, 4], 程序实现: 删除lst元素中的最大值和最小值（不考虑多个最值情况）

lst = [1, 3, 2, 6, 4]
lst.sort()
lst.pop(0)
lst.pop(len(lst)-1)
print(lst)

# 已知 lst = [1, 3, 2, 6, 1, 1, 41], 程序实现: 求lst中最后一个为1的元素的索引

lst = [1, 3, 2, 6, 1, 1, 41]
      #  0  1  2  3  4  5  6  orginal
      #  6  5  4  3  2  1  0  reverse
print(len(lst)-1 - lst[::-1].index(1))
str = str(lst)
 
"""
编写程序实现: 请用户输入用逗号隔开的一串数字, 输出转化成元组后的数据

例:
用户输入:  1,2,3,45,678
程序输出:  ('1', '2', '3', '45', '678')
"""
tup = tuple(input('请用户输入用逗号隔开的一串数字: ').split(','))
print(tup)
