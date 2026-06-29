
# #转换age值类型为整形进行判断
#
# age = int(input('请输入你的年龄：'))
# if age >= 18:
#     print('你是成年人')
#     print('成年人的世界，虽不容易，但很精彩！')
# print('欢迎你来学习Python！')

# age = int(input('请输入你的年龄：'))
# if age >= 18:
#     print('你是成年人')
#     print('成年人的世界，虽不容易，但很精彩！')
# else:
#     print('你是未成年人')
#     print('好好加油，努力学习，未来可期！')
# print('欢迎你来学习Python！')

# 根据年龄来判断处于人生哪个阶段。
age = int(input('请输入你的年龄：'))
if age <= 10:
    print('你是幼儿')
elif age <= 18:
    print('你是青少年')
elif age <= 30:
    print('你是青年')
elif age <= 50:
    print('你是中年')
elif age <= 60:
    print('你是中老年')
else:
    print('你是老年')