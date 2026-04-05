""""""
"""
字符串（String）
    - 特性：不可变，是序列
    - 单行字符串：用一对引号定义
    - 多行字符串：用成对的三个引号定义 
"""

emptyStr = ""
print(emptyStr)

spaceStr = ' '
print(spaceStr)
# 单行字符串
str1 = 'Hello World'
print(str1)

str2 = 'Hello World'  # 单行字符串
print(str2)

print(str1 == str2)

print(str1 is str2)

str3 = '''Hello World'''  # 多行字符串
print(str3)

print(str1 == str3)
print(str1 is str3)

str4 = """Hello World"""  # 多行字符串
print(str4)

str5 = '''hello
world
，,：:！!
123
🐕🐬🐛'''
print(str5)

str6 = """hello
world
，,：:！!
123
🐕🐬🐛"""
print(str6)

print('---------------------------------------------------------------------')
"""
str(obj)
    将obj对象转化为字符串形式并返回
"""
print(str())  # ''
print(str('hello'))  # 'hello'
print(str(1234))  # '1234'
print(str(-1.23))  # '-1.23'
print(str(True))  # 'True'

# 转化complex后自动加括号？
print(str(3 + 4J))  # '(3+4j)'
complex1 = 1 + 3j
print(str(complex1))
print('---------------------------------------------------------------------')

"""
转义字符
    在字符串中，反斜杠和某些字符组成得特殊序列叫做转义字符。
    Demo：
        请输出以下文字：
            小明说:'我叫小明,你叫什么？',那人回答道:"我叫小帅"
"""
# 利用多行字符串的方式
print('''小明说:'我叫小明,你叫什么？',那人回答道:"我叫小帅"''')
# 使用转义字符方式
print('小明说:\'我叫小明,你叫什么？\',那人回答道:"我叫小帅"')

'''
输出：
    反斜杠是:'\'
'''
print("""'\\'""")  # \ 的转义符是\\

'''
\n 换行符
输出：
    Hello World
    Hello Python
'''
print('''Hello World
Hello Python''')
print('''Hello World\nHello Python''')

'''
横向制表符 \t

相当于加Tab

'''
print('A\tBCDEFGHIJ')
print('AB\tCDEFGHIJ')
print('ABC\tDEFGHIJ')
print('ABCDEFG\tHIJ')
print('ABCDEFGH\tIJ')
print('---------------------------------------------------------------------')

'''
原始字符
    给字符串添加前缀r或R来声明，原始字符串中的反斜杠保留原样，不再触发转义行为。
    注意：字符串末尾不能存在奇数个反斜杠，会引发语法错误。
'''
print('https:\\www.example.com\nuxy\tngj')
print(r'http :\\www.example.com\nuxy\tngj')
print('---------------------------------------------------------------------')

"""
字符串格式化
    %s：格式化为字符串，适用于任何对象
    %d、%i：格式化为整数，仅适用于数字
    %f、%F：格式化为浮点数，默认精确到小数点后六位，仅适用于数字
"""
print('我有一只宠物叫：%s，今年%d岁了，每天的饭量大概是%f克' % ('金桔', 1.02, 3.141592653))
print('我有一只宠物叫：%s，今年%d岁了，每天的饭量大概是%f克' % ('金桔', 1.02, 3.14))  # 浮点数会自动补全后六位
# 自定义保留小数点后几位，使用 %.nf，如保留后三位%.3f
print('我有一只宠物叫：%s，今年%d岁了，每天的饭量大概是%.3f克' % ('金桔', 1.02, 3.1415))

'''
format方法格式化
'''
print('我有一只宠物叫：{}，今年{}岁了，每天的饭量大概是{}克'.format('金桔', 1.02, 3.1415))

name = '旺财'
year = 2.8
hour = 8.547

# 传位置参数, 实参按照从左往右的顺序传入占位符{}
print('它叫{}, 我养了它{}年, 它每天睡{}小时!'.format(name, year, hour))
# 传关键字参数
print('它叫{n}, 我养了它{y}年, 它每天睡{h}小时!'.format(y=year, h=hour, n=name))
# 根据实参的下标传参
print('它叫{2}, 我养了它{0}年, 它每天睡{1}小时!'.format(year, hour, name))
# {:.nf}表示精确到小数点后n位
print('它叫{}, 我养了它{}年, 它每天睡{:.2f}小时!'.format(name, year, hour))

'''
f-string格式化
'''
print(f'它叫{name}, 我养了它{year}年, 它每天睡{hour}小时!')

# {:.nf} 表示精确到小数点后n位
print(f'它叫{name}, 我养了它{year}年, 它每天睡{hour:.2f}小时!')

"""
字符串方法
"""
print("--------------------------------字符串方法-------------------------------------")
"""
    str.replace(old, new, count=-1) #replace old character with new character
      - old: 旧字符串
      - new: 新字符串
      - count: 要替换的最大次数，默认不限制
      - 用新字符串替换旧字符串并返回
"""
s = 'Line1 Line2 Line3 Line4'
# 用 "b" 替换所有的 "Li"
print(s.replace("Li", "b"))  # bne1 bne2 bne3 bne4
# 用 "b" 替换所有的 "Li",最多两次
print(s.replace('Li', 'b', 2))  # bne1 bne2 Line3 Line4
print('--------------------------------------------------------')

"""
    str.strip([chars])
      - chars: 指定要移除的字符，如果没有指定则默认移除空白符（空格符、换行符、制表符）
      - 删除字符串左右两边指定的字符
"""
# 删除字符串两边的空白符
str1 = ' \thello wrold h \n'
print(str1.strip())  # hello wrold h

# 删除字符串两边的'o'字符
str2 = "ooho hello wrold"
print(str2.strip('o'))  # ho hello wrold

# 删除字符串两边的'c','w','o','m'字符
str3 = 'www.example.com'
'''
注意：
    参数 cwom 是一个字符串，并不是一个元组
    但是方法匹配的并不是整一个字符串，而是这个字符串的字符集 - c w o m
'''
print(str3.strip("cwom"))  # .example.
print('--------------------------------------------------------')

"""
    str.startswith(prefix[, start[, end]])
        - prefix：匹配的前缀，可以是字符串或者字符串组成的元组（元组中只要一个元素满足即可） 
        - start：开始索引，不指定则默认为0
        - end：结束索引（开区间），不指定则默认为 len(str)
        - 判定字符串是否以 prefix 指定的值开始（start和end参数用来控制字符串的判定区间）
"""
str1 = "hello world"
print(str1.startswith("h"))  # True
print(str1.startswith("he"))  # True
print(str1.startswith("wo"))  # False
print(str1.startswith("wo", 6))  # True
'''
    下面startswith方法中的参数是传入一个字符串元组(集合)，对参数的处理方式是完整的字符串匹配
    与strip("abc") 有所不同，strip是对字符串中的字符集做匹配
    
    startswith - "starts with this exact string"
    "hello".startswith("he")     # 问：是不是以 "he" 开头？
    
    strip - "strip these characters"  
    "hello".strip("he")          # 做：删除所有 'h' 和 'e'
'''
print(str1.startswith(("wo", "h")))  # True
print('--------------------------------------------------------')

"""
str.endswith(suffix[, start[, end]])
    - suffix：匹配的后缀，可以是字符串或者字符串组成的元组（元组中只要一个元素满足即可） 
    - start：开始索引，不指定则默认为0
    - end：结束索引（不包括该索引），不指定则默认为 len(str)
    - 判定字符串是否以 suffix 指定的值结束（start和end参数用来控制字符串的判定区间）
"""
str1 = "hello world"
print(str1.endswith("d"))  # True
print(str1.endswith("ld"))  # True
print(str1.endswith("lo"))  # False
print(str1.endswith("lo", 1, 5))  # True
"""
不管是startswith 还是endswith方法，其中的索引参数end都是不包含关系，即：
    范围：[start, end) 从 start 到 end-1
可以使用str[start:end] 做测试，如：
str = 'hello world'
str[0:3] = 'hel'
str[3:6] = 'lo '
"""
print(str1.endswith(("d", "lo")))  # True
str1 = 'hello world'
print(str1[0:3])  # 'hel'
print(str1[3:6])  # 'lo '
print('--------------------------------------------------------')

"""
str.isdigit()
    - 判定字符串中的每个字符是否都为数字型的字符
"""
string = '1234'
print(string.isdigit())  # True

string = '-123'
print(string.isdigit())  # False

string = '1.23'
print(string.isdigit())  # False
print('--------------------------------------------------------')

"""
str.split(sep=None, maxsplit=-1)
    - sep：分隔符,  不指定时默认为所有的空白符（空格、换行、制表符）, 并丢弃结果中的空字符串
    - maxsplit：最大分隔次数，默认不限制
    - 通过指定的分隔符对字符串进行分割，以列表的形式返回
    
    开头有分隔符 → 前面加空 ''
    中间连续分隔符 → 中间加空 ''
    结尾有分隔符 → 默认不加空（除非用 split(' ', -1)）
"""
s = " Line1  \nLine2   \tLine3"
print(s.split())
# ['Line1', 'Line2', 'Line3']
# 解释：
# - 开头的空格被忽略
# - \n 作为分隔符
# - 连续的空格被合并处理
# - 制表符\t作为分隔符
# - 没有空字符串

# 带空格参数：严格按空格
print(s.split(' '))
# ['', 'Line1', '', '\nLine2', '', '', '\tLine3']
# 解释：
# - 开头空格 → ''
# - 连续两个空格 → 中间产生 ''
# - 空格和\n之间 → 产生 ''
# - 等等...


print(s.split('Li'))
# [' ', 'ne1  \n', 'ne2   \t', 'ne3']

print(s.split('Li', 2))
# [' ', 'ne1  \n', 'ne2   \tLine3']
print('--------------------------------------------------------')

"""
str.join(iterable)

    - iterable：包括str、list、tuple、dict、set等
    - 将可迭代对象中的元素（元素必须是字符串）以指定的字符串连接，返回新的字符串
"""

s = '-.'

s1 = 'hello world'
print(s.join(s1))  # h-.e-.l-.l-.o-. -.w-.o-.r-.l-.d

s2 = ['1', '2', '3', '4']
print(s.join(s2))  # 1-.2-.3-.4

s3 = ('1', '2', '3', '4')
print(s.join(s3))

'''
---------------------------------------------------------------------------
特性	            s2 = ['1', '2', '3', '4']   	s3 = ('1', '2', '3', '4')
类型	            列表 (list)	                    元组 (tuple)
符号	            方括号 []	                    圆括号 ()
可变性	        ✅ 可修改	                    ❌ 不可修改
可添加元素	    ✅ 可以	                        ❌ 不可以
可删除元素	    ✅ 可以	                        ❌ 不可以
可排序	        ✅ 可以	                        ❌ 不可以
内存占用	        较大	                            较小
创建速度	        较慢	                            较快
---------------------------------------------------------------------------
'''
# 字典作为iterable, 只有键参与迭代
s4 = {'height': 175, 'weight': 65}
print(s.join(s4))  # height-.weight

s5 = {'5', 'hello', '789', 'world'}
print(s.join(s5))  # 5-.hello-.789-.world
print('--------------------------------------------------------')

"""
str.count(sub, [start[, end])
    - sub：需要查找的字符串
    - start：开始索引，默认为0
    - end：结束索引（开区间），默认为 len(str)
    - 返回 sub 在字符串中出现的次数
"""
s = "hello world"
print(s.count('l'))  # 3
print(s.count('lo'))  # 1
print(s.count('ol'))  # 0
print('--------------------------------------------------------')

"""
str.find(sub[, start[, end]])
返回从左边开始第一次找到指定字符串时的正向索引，找不到就返回 -1

str.rfind(sub[, start[, end]])
返回从右边开始第一次找到指定字符串时的正向索引，找不到就返回 -1

str.index(sub[, start[, end]])
类似于find()，唯一不同在于，找不到就会报错

str.rindex(sub[, start[, end]])
类似于rfind()，唯一不同在于，找不到就会报错

- sub：需要查找的字符串
- start：开始索引，默认为0
- end：结束索引（开区间），默认为 len(str)
"""
s = 'hello world'
#    索引: 0  1  2  3  4  5  6  7  8  9  10
#    字符: h  e  l  l  o     w  o  r  l  d

print(s.find('l'))  # 2
print(s.rfind('l'))  # 9
print(s.find('lo'))  # find() 返回子串第一次出现时，第一个字符的索引 所以结果是3
print(s.rfind('lo'))  # 3
print(s.index('l'))  # 返回找到的第一个 l 的索引
print(s.rindex('l'))  # 9
print(s.index('lo'))  # 3
print(s.rindex('lo'))  # 3
print(s.find('ol'))  # -1
print(s.rfind('ol'))  # -1

print('--------------------------------------------------------')
"""
str.capitalize()
将字符串的首字母变成大写，其他字母变小写，并返回

str.title()
将字符串中所有单词的首字母变成大写，其他字母变小写，并返回

str.upper()
将字符串中所有字符变成大写，并返回

str.lower()
将字符串中所有字符变成小写，并返回

str.swapcase()
将字符串中所有大写字符变成小写，小写变成大写，并返回
"""
s = '你好hELlo wo?rLD世界TuP'
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())

print('--------------------------------------------------------')
