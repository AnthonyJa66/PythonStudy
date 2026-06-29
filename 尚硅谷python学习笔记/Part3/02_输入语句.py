
#默认input输入值为字符串类型
age=input("请输入你的年龄：")
name=input("请输入你的名字：")
# print(type(age))

#将字符串转换为整形
age=int(age)
print(f"你的名字是{name}，明年的年龄是：{age+1}")
