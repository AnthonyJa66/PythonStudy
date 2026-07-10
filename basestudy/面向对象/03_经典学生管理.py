class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={"语文":0,"数学":0,"英语":0}#字典

    def set_grades(self,course,grade):
        if course in self.grades:
            self.grades[course]=grade

    def print_grades(self):
        print(f'{self.name}的学号为：{self.student_id},成绩为：{self.grades}')
        for course in self.grades:
            print(f'{course}分数为{self.grades[course]}分')


chen=Student("陈三",1001)
zhang=Student("张三",1002)

# print(chen.name)
# print(zhang.grades)
zhang.set_grades("语文",90)
print(zhang.grades)
zhang.print_grades()
