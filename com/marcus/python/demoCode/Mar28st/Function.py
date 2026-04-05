"""
- 函数让程序更加模块化，可读性更强且易于复用

- 形参：形式参数，函数在定义时声明的参数

- 实参：实际参数，函数在调用时传入的参数

- 函数体：函数的具体内容，它决定了函数的功能

- 函数在定义时，不会执行函数体；当函数被调用时，才会执行函数体

- 函数只需要定义一次，就可以被多次调用

- 函数每次被调用时，都会把实参传递给对应的形参，然后执行函数体

- 定义函数的语法

  def func_name(par1, par2, ..., parN):

- 调用函数的语法

  func_name(arg1, arg2, ..., argN)
"""


def functionDemo(x, y, z):
    print(2 * x + 3 * y - z + 4 * z + 5 * x + 6)


"""
传位置参数：实参会按照从左往右的顺序依次传递给形参
"""
functionDemo(1, 2, 3)
functionDemo(3, 2, 1)

"""
传关键字参数：实参会根据指定的名称传递给同名的形参（与位置顺序无关）
"""
functionDemo(x=1, z=2, y=3)
functionDemo(z=3, y=2, x=1)

"""
注意：所有的关键字参数必须放在所有位置参数的后面
"""
functionDemo(1, z=3, y=2)
# functionDemo(3, x=1, y=2) # 这样写会报错
functionDemo(1, 2, z=3)

"""
函数是否有返回值，取决于关键字return
如果函数没有返回值，等价于return none
return的作用：将它后面的对象返回给函数调用方，函数调用方就变成了该对象，并且将所在的函数结束
"""
print('--------------------------------------------------')


def functionDemo1(x, y, z):
    return 2 * x + 3 * y - z + 4 * z + 5 * x + 6


result = functionDemo1(1, 2, 3)

print(result)

print(result * 2)

print(result / 2)

result1 = functionDemo(1, 2, 3)

print('-------------------------------------------------')
print(result1)

print(functionDemo(1, 2, 3))
