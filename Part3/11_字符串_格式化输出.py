name = '张三'
gender = '男'
weight = 68.45
age = 20
work_age = 2

# 写法1
info1 = '我是' + name + '，性别' + gender
print(info1)

# 写法2 占位符
info2 = '我是%s，性别%s，体重%f，年龄%i，工龄%d年' % (name, gender, weight, age, work_age)  # 整数可以%i表示int整形，也可以%d表示十进制
print(info2)
#print(type(info2))

info3 = '我是%s，性别%s，体重%i，年龄%i，工龄%i年' % (name, gender, weight, age, work_age)
print(info3)

# 写法3 f-string  官方推荐方式
info4 = f'我是{name}，性别{gender}，体重{weight}，年龄{age}，工龄{work_age}年'
print(info4)
