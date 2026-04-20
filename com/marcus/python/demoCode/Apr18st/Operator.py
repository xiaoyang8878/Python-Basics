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

str1 = 'hello '
str2 = 'world'
print(str1 + str2)
str1 += str2
print(str1)

str1 = 'hello '
print(str1 * 3)
str1 *= 3
print(str1)


lst1 = [1, 2]
lst2 = [3, 4, 5]
print(lst1 + lst2)
lst1 += lst2
print(lst1)

lst1 = [1, 2]
print(lst1 * 3)
lst1 *= 3
print(lst1)


tup1 = (1, 2)
tup2 = (3, 4, 5)
print(tup1 + tup2)
tup1 += tup2
print(tup1)

tup1 = (1, 2)
print(tup1 * 3)
tup1 *= 3
print(tup1)