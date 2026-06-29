# /和*分别限制传入位置参数和关键字参数
# 定义函数
def greet(name,gender,*, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')

# 调用函数（使用关键字参数）
# greet(name='张三', gender='男', age=18, height=172)
greet(height=172, age = 18, gender='男', name='张三')