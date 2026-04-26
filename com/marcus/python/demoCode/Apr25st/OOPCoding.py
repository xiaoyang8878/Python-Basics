"""
面向过程编程
    围绕着“怎么做”展开
    强调步骤分解
    这样编写的程序，可读性比较好，程序的性能会好点，但是程序的耦合度过高，不利于程序的后期修改
    所以面向过程编程更适合一些简单的，线性的，偏底层的，代码不需要经常修改的场景

面向对象编程
    围绕着“谁来做”展开
    强调职责分配
    这样编写的程序可读性稍差，代码量相对会多一点，程序的性能会相对差一点
    但是可以大大的降低代码的耦合度，更有利于程序的后期维护，
    所以面向对象编程更适合一些复杂的场景
"""

"""
__new__: 该魔术方法在实例化时自动触发，称为构造方法，用来创建实例对象，并返回该实例对象
__init__: 该魔术方法在实例化时自动触发，称为初始化方法，可以对实例对象进行属性定制，没有返回值

每次实例化的时候，都会先自动调用__new__(clz, *args, **kwargs)方法，把要实例化的类对象作为实参传递给形参clz，
实例化传入的实参传递给实参*args, **kwargs，然后__new__方法会根据形参clz接收到的类对象创建一个对应的实例对象，并返回该实例对象

接着，实例化过程会自动调用__init__(self, name, age, score)方法，逻辑是把__new__方法构建的实例对象传递给self，实例化时传入的
其他实参('张三', 30, 100)转给形参name, age, score，然后__init__方法在对形参self接收到的实例对象做属性定制(inplace操作)

"""


class Person(object):
    name = ''
    age = ''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def wake_up(self):
        print(f'{self.name}睁开眼睛、起身、穿好衣服')

    def wash(self):
        print(f'{self.name}刷牙洗脸')

    def eat(self):
        print(f'{self.name}吃菜扒饭')

    def sleep(self):
        print(f'{self.name}脱掉外套、躺下、闭眼睡觉')

    def show_time(self):
        print(f'{self.name}')


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade


    def login(self):
        print(f'{self.name}输入账号密码、登录学习平台')

    def study(self):
        print(f'{self.name}的学习任务就是看视频查资料写代码')


class Teacher(Person):
    def __init__(self, department):
        self.department = department
        self.name = super().name
        self.age = super().age

    def punch_in(self):
        print(f'{self.name}打卡上班')


stu1 = Student('张三', 18, '大一')

print(stu1.grade, stu1.name, stu1.age)
