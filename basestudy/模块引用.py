#方式一：引用statistics模块中的所有函数，但需要statistics.函数名调用
# import statistics
# #引用模块中的函数median
# print(statistics.median([1,2,3,4,5,6,7,8,9]))

# #方式二：引用statistics模块中的函数mean,median，但不需要statistics.函数名调用
# from statistics import mean,median
# #mean()函数：计算平均数
# print(mean([1,2,3,4,5,6,7,8,9]))
# #median()函数：计算中位数
# print(median([1,2,3,4,5,6,7,8,9]))


#方式三：引用statistics模块中的所有函数，但不需要statistics.函数名调用
from statistics import*
print(mean([1,2,3,4,5,6,7,8,9,10]))
print(median([1,2,3,4,5,6,7,8,9]))
