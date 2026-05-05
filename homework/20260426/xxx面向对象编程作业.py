"""
题目: 请设计一个学生管理系统, 包含一下内容:

1. 学生类(Student):
   - 包括属性: 学生姓名(name)、学生年龄(age)、学生成绩(score)
   - 包括功能:
     - 获取学生信息(get_info): 返回该学生的姓名、年龄和成绩。

2. 班级类(ClassRoom):
   - 包括属性: 班级名称(name)、班级学生列表(students)、所有班级列表(classes)
   - 包括功能: 
     - 添加学生(add_student): 将学生对象添加到指定班级的学生列表中, 如果该学生已经在指定班级中则无需重复添加, 如果该学生在其它班则调班。
     - 移除学生(remove_student): 将学生对象从指定班级的学生列表中移除, 如果该学生不在指定班级则无需移除。
     - 获取指定班级的学生信息(get_students_info): 输出指定班级的所有学生信息, 如果没有指定班级, 则默认输出所有班级的所有学生信息。

要求: 
1. 实现上述内容。
2. 编写相关测试代码。
"""

import random


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.score = score
        self.age = age

    def get_info(self):
        return f"姓名: {self.name}, 年龄: {self.age}, 成绩: {self.score}"


class ClassRoom:
    """
    我认为ClassRoom这个对象应该专注于管理学生，班级列表不应由班级对象管理，应交由学校School管理
    """

    def __init__(self, name, students):
        self.name = name
        self.students = students

    def add_student(self, stu):  # 将学生对象添加到指定班级的学生列表中, 如果该学生已经在指定班级中则无需重复添加, 如果该学生在其它班则调班。
        if stu not in self.students:
            self.students.append(stu)
            print(f'!!!!!!!学生：{stu.name}已添加到班级{self.name}中!!!!!!!')

    def remove_student(self, stu):  # 将学生对象从指定班级的学生列表中移除, 如果该学生不在指定班级则无需移除。
        if stu in self.students:
            print(f"!!!!!!!学生：{self.students.pop(self.students.index(stu)).name} 已从班级{self.name}移除!!!!!!!")

    def get_students_info(self):  # 输出指定班级的所有学生信息, 如果没有指定班级, 则默认输出所有班级的所有学生信息。
        print(f"\n【{self.name}】班级学生信息:")
        for stu in self.students:
            print(f"  {stu.get_info()}")


class ClassRoom2():
    """
    不使用School类管理班级，则将所有班级放置在类属性classes中
    """

    classes = {}

    def __init__(self, name):
        if name in ClassRoom2.classes:
            print(f"班级{name}已存在")
        self.name = name
        self.students = []
        ClassRoom2.classes[name] = self

    def add_student(self, stu):
        # 判断该学生是否在其他班级中
        for key, value in ClassRoom2.classes.items():
            if key == self.name and stu in value.students:
                return f'学生{stu.name}已存在班级{self.name}中，需要调班'
        if stu not in self.students:
            self.students.append(stu)
            return f'学生{stu.name}添加到班级{self.name}成功'

    def remove_student(self, stu, class_name):  # 将学生对象从指定班级的学生列表中移除, 如果该学生不在指定班级则无需移除。

        class_room = ClassRoom2.classes[class_name]
        class_stus = class_room.students

        if stu in class_stus:
            print(f'学生{self.students.pop(self.students.index(stu)).name}已移除出班级{class_name}')

    def get_students_info(self, class_name=''):
        if class_name == '':
            for key, value in ClassRoom2.classes.items():
                print(f"\n【{key}】班级学生信息:")
                stus = value.students
                for stu in stus:
                    print(stu.get_info())
        else:
            stus = ClassRoom2.classes[class_name].students
            print(f"\n【{class_name}】班级学生信息:")
            for stu in stus:
                print(stu.get_info())

    def tran_class(self, stu, to_class):
        # 检查目标班级是否存在
        if to_class not in ClassRoom2.classes:
            return f"班级{to_class}不存在"

        # 检查学生是否在当前班级
        if stu not in self.students:
            return f"学生{stu.name}不在当前班级{self.name}中"

        # 从当前班级移除
        self.students.remove(stu)

        # 添加到目标班级
        target_class = ClassRoom2.classes[to_class]
        target_class.students.append(stu)

        return f"学生{stu.name}已从{self.name}转到{to_class}"


class School:

    def __init__(self, name):
        self.name = name
        self.classes = []

    def add_class(self, classroom):
        if classroom not in self.classes:
            self.classes.append(classroom)

    def transfer_student(self, stu, from_class, to_class):
        """调班功能"""
        if from_class:
            from_class.remove_student(stu)
        to_class.add_student(stu)

    def get_all_students_info(self):
        """获取所有班级的学生信息"""
        print(f"\n========== {self.name} 全部班级信息 ==========")
        for cls in self.classes:
            cls.get_students_info()


if __name__ == "__main__":

    # class_rooms = []
    #
    # for j in range(5):
    #     students = []
    #     for i in range(0, 10):
    #         random_score = random.randint(1, 100)
    #         random_age = random.randint(6, 22)
    #         student = Student(('stu' + str(i + 1)), random_age, random_score)
    #         students.append(student)
    #     class_room = ClassRoom(('classroom' + str(j + 1)), students)
    #     class_rooms.append(class_room)
    #
    # for cls_room in class_rooms:
    #     cls_room.get_students_info()

    students1 = []
    students2 = []
    stuA = Student('张三', random.randint(6, 22), random.randint(1, 100))
    stuB = Student('李四', random.randint(6, 22), random.randint(1, 100))
    for i in range(0, 10):
        random_score = random.randint(1, 100)
        random_age = random.randint(6, 22)
        student = Student(('stu' + str(i + 1)), random_age, random_score)
        students1.append(student)
        students2.append(student)

    # Student的get_info()
    for student in students1:
        print(student.get_info())

    print('-----------------------------------------------------------------------------------------------------------')

    # ClassRoom的add_student()
    class_roomA = ClassRoom('Class RoomA', students1)
    class_roomB = ClassRoom('Class RoomB', students2)
    class_roomA.add_student(stuA)
    class_roomA.get_students_info()
    class_roomB.add_student(stuB)
    class_roomB.get_students_info()
    print('-----------------------------------------------------------------------------------------------------------')

    # remove_student()
    # class_roomA.remove_student(stuA)
    # class_roomA.remove_student(stuB)
    # class_roomA.get_students_info()
    # class_roomB.get_students_info()
    print('-----------------------------------------------------------------------------------------------------------')

    # School
    school = School('春天花花幼稚园')
    school.add_class(class_roomA)
    school.add_class(class_roomB)
    school.transfer_student(stuA, class_roomA, class_roomB)
    school.transfer_student(stuB, class_roomB, class_roomA)
    school.get_all_students_info()

    print('-----------------------------------------------------------------------------------------------------------')
    # ClassRoom2
    class_room1 = ClassRoom2('Class1')
    class_room1.students = students1

    class_room2 = ClassRoom2('Class2')
    class_room2.students = students2

    class_room1.get_students_info()

    class_room2.get_students_info('Class1')

    print(class_room1.add_student(stuA))

    print(class_room2.add_student(stuB))

    print(class_room1.add_student(stuA))

    class_room1.remove_student(stuA, 'Class1')
    class_room1.remove_student(stuA, 'Class2')

    print(class_room2.tran_class(stuB, 'Class2'))
