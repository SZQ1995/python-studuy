"""
学生管理类
"""
from test_case.student import Student


class StudentManager():

    def __init__(self):
        self.stuList = []

    def add_stu(self):
        # 提示用户输入学员信息
        name = input('请输入学员的姓名：')
        age = int(input('请输入学员的年龄：'))
        mobile = input('请输入学员的电话：')
        s = Student(name, age, mobile)
        self.stuList.append(s)
        print('学员信息添加成功')

    def delete_stu(self):
        name = str(input('请输入删除的名字'))
        for i in self.stuList:
            if name == i.name:
                self.stuList.remove(i)
                break
        else:
            print('您要刪除的学员不存在')

    def update_stu(self):
        name = input('请输入要修改的学员姓名：')
        for i in self.stuList:
            if name == i.name:
                i.name = input('请输入修改后的学员姓名：')
                i.age = int(input('请输入修改后的学员年龄：'))
                i.mobile = input('请输入修改后的学员电话：')
                print(
                    f'学员信息修改成功，修改后信息如下 => 学员姓名：{i.name}，学员年龄：{i.age}，学员电话：{i.mobile}')
                break
        else:
            print('您要修改的学员不存在')

    def show_stu(self):
        # 提示用户输入要查询的学员姓名
        name = input('请输入要查询的学员姓名：')
        # 对student_list属性进行遍历
        for i in self.stuList:
            if i.name == name:
                print(i)
                break
        else:
            print('您要查找的学员信息不存在...')

    def show_all(self):
        for i in self.stuList:
            print(i)

    # 保存学员信息到文件
    def save_student(self):
        # 打开文件
        try:
            f = open('student.txt', 'w')
            list = [i.__dict__ for i in self.stuList]
            f.write(str(list))
        except Exception as e:
            print('写入出错')
        finally:
            f.close()

    @staticmethod
    def show_help():
        print('-' * 40)
        print('传智教育通讯录管理系统V2.0')
        print('1.添加学员信息')
        print('2.删除学员信息')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        # V2.0新增功能
        print('6.保存学员信息')
        print('7.退出系统')
        print('-' * 40)

        # 定义load_student()方法

    def load_student(self):
        try:
            f = open('student.txt', 'r', encoding='utf-8')
            self.stuList = []
        except:
            f = open('student.txt', 'w', encoding='utf-8')
        else:
            content = f.read()
            if len(content)==0:
                return
            # 把字符串转换为原数据类型[{}, {}, {}]
            data = eval(content)
            self.stuList = [Student(i['name'], i['age'], i['tel']) for i in
                            data]
        finally:
            f.close()

    # 定义一个run()方法，专门用于实现对管理系统中各个功能调用
    def run(self):
        # 1、调用一个学员加载方法，用于加载文件中的所有学员信息，加载完成后，把得到的所有学员信息保存在student_list属性中
        self.load_student()
        # 2、显示帮助信息，提示用户输入要实现的功能编号
        while True:
            self.show_help()
            user_num = int(input('请输入要操作功能的编号：'))
            if user_num == 1:
                self.add_stu()
            elif user_num == 2:
                self.delete_stu()
            elif user_num == 3:
                self.update_stu()
            elif user_num == 4:
                self.show_stu()
            elif user_num == 5:
                self.show_all()
            elif user_num == 6:
                self.save_student()
            elif user_num == 7:
                print('感谢您使用传智教育通讯录管理系统V2.0，欢迎下次使用！')
                break
            else:
                print('信息输入错误，请重新输入...')
