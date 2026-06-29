# 定义一个成绩列表
score_list = [62, 50, 60, 48, 80, 20, 95]

# # 使用while循环遍历列表
# index = 0
# while index < len(score_list):
#     print(score_list[index])
#     index += 1

# # 使用for循环遍历列表
# for item in score_list:
#     print(item)

for index in range(len(score_list)):
    print(index,score_list[index])

# for index,item in enumerate(score_list,start=3):
#     print(index,item)
#
# print(score_list[0])