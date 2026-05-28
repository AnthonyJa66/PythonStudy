# # for嵌套循环实现打印训练计划
# day = 1
# for day in range(1, 8):
#     print(f'这是第{day}天训练')
#     for group in range(1, 4):
#         if day % 2 == 1 and group % 2 == 0:
#             print(f'❌这是第{day}天，第{group}组训练未完成')
#         else:
#             print(f'💪这是第{day}天，第{group}组训练')
#
# print(f'🎉为期{day}天训练计划完成')


# # while循环实现
# d=1
# while d<8:
#     print(f'这是第{d}天训练')
#
#     g = 1 #嵌套循环要把变量放进来，每次外层循环时都刷新值
#     while g<4:
#         print(f'💪这是第{d}天，第{g}组训练完成')
#         g += 1
#     d+=1
#
# print(f'🎉为期{d-1}天训练计划完成')
