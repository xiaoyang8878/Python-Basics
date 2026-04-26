'''
条件语句
    格式一
        if 判断条件:
            执行代码块

	格式二
        if 判断条件:
            执行代码块1
        else:
            执行代码块2

	格式三
	    if 判断条件1:
		    执行代码块1
        elif 判断条件2:
            执行代码块2
        elif 判断条件3:
            执行代码块3
        ...
        else:
            执行代码块n
'''

d = {'石头': 0, '剪刀': 1, '布': 2}

player = input('请您出拳（石头 剪刀 布）：')
computer = set(d).pop()  # 集合本身就是无序的，删除第一个元素并返回

player_num = d[player]
computer_num = d[computer]

if player_num - computer_num in (-1, 2):
    print(f'玩家出的是{player}, 电脑出的是{computer}, 玩家胜')
elif player_num - computer_num == 0:
    print(f'玩家出的是{player}, 电脑出的是{computer}, 平局')
else:
    print(f'玩家出的是{player}, 电脑出的是{computer}, 电脑赢')

