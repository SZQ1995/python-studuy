
"""
学生类
"""
class Student():
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel

    def __str__(self):
        return f"{self.name},{self.age},{self.tel}"

        