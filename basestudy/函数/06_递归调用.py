#递归必须要具备终止条件（不能无限的一直调用，总得有停下来的时候。）

# 使用递归打印n次“你好啊”（从大到小）
# def welcome(n):
#     print(f'你好啊{n}')
#     if n > 1:
#         welcome(n - 1)
# # 调用函数
# welcome(5)

# # 使用递归打印n次“你好啊”（从小到大）
# def welcome(n):
#     if n > 1:
#         welcome(n - 1)
#     print(f'你好啊{n}')
# # 调用函数
# welcome(5)


# # 使用递归求阶乘
# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)
# # 调用函数，求5的阶乘
# result = factorial(6)
# print(result)

def factorial(n):
    if n==0:
        return 1

    else:
        return n * factorial(n-1)#6*5*4*3*2*1

factorial(8)
print(factorial(8))
