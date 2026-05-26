name = '张三'
gender = '男'
weight = 68.56
age = 20
work_age = 2.65

# 占位符精度控制
# 整数可以%i表示int整形，也可以%d表示十进制
info = '我是%s，性别%s，体重%f，年龄%i，工龄%d年' % (name, gender, weight, age, work_age)
print(info)

#占位符  %m.n   m指的是占几位，+-代表靠右和靠左对齐，n代表保留几位空格/小数点后几位
info1 = '我是%-3.3s，性别%s，体重%4.2f，年龄%i，工龄%d年' % (name, gender, weight, age, work_age)
print(info1)
