d = {'石头': 0, '剪刀': 1, '布': 2}

computer = set(d).pop()
print(computer)
player = input('请出拳(石头、剪刀、布): ')

# 出拳展示
print(f'电脑出拳: {computer}\n玩家出拳: {player}')

# 胜负判定
c, p = d[computer], d[player]
if p-c in (-1, 2):
    print('玩家胜!')
elif c == p:
    print('平局!')
else:
    print('电脑胜!')