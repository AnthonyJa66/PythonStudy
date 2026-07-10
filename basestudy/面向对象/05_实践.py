# 类继承练习:人力系统
#
# 员工分为两类:全职员工 FullTimeEmployee、兼职员工 PartTimeEmployee。
#
# 全职和兼职都有"姓名 name"、"工号 id"属性,
#
# 都具备"打印信息 print_info"(打印姓名、工号)方法。
#
# 全职有"月薪 monthly_salary"属性，I
#
# 兼职有"日薪 daily_salary"属性、"每月工作天数 work_days"的属性。
#
# 全职和兼职都有"计算月薪 calculate_monthly_pay"的方法，但具体计算过程不一样。
from torch.onnx.symbolic_opset8 import full


class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def print_info(self):
        print(f'{self.name}的工号是:{self.id}')


class FulltimeEmployee(Employee):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)#super()函数在自己的构造函数中调用父类的构造函数，同时还能在下方添加自己需要的属性
        self.monthly_salary=monthly_salary
        self.print_info()
        self.calculate_monthly_pay()


    def calculate_monthly_pay(self):
        print(f'{self.name}是全职员工，月薪是:{self.monthly_salary}')



class ParttimeEmployee(Employee):
    def __init__(self,name,id,daily_salary,work_days):
        super().__init__(name,id)#super()函数在自己的构造函数中调用父类的构造函数，同时还能在下方添加自己需要的属性
        self.daily_salary=daily_salary
        self.work_days=work_days
        self.print_info()
        self.calculate_monthly_pay()

    def calculate_monthly_pay(self):
        print(f'{self.name}是兼职员工，月薪是:{self.daily_salary*self.work_days}')
        return self.daily_salary*self.work_days


a=FulltimeEmployee('张三',1001,5000)
b=ParttimeEmployee('李四',1002,100,20)
print(b.calculate_monthly_pay())
