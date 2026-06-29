#元组：用来存放一组有序的数据，但其中的内容一旦创建就不可修改（不能增、删、改，只能查）。
# 由于元组不可变，所以元组不能使用append()、insert()这些方法，它里面的元素也不能被重新赋值。

# 定义有内容的元组
t1 = (28, 67, 21, 67, 11)
t2 = ('北京', '尚硅谷', '你好')
t3 = (100, True, '你好', None)
t4 = (100, True, '你好', None, (50, 60, 70))
# print(type(t1), t1,t1[2])
# print(type(t2), t2)
# print(type(t3), t3)
# print(type(t4), t4)

# # 定义空元组
# t1 = ()
# t2 = tuple()
# print(type(t1), t1)  # <class 'tuple'> ()
# print(type(t2), t2)  # <class 'tuple'> ()

# t5=(5,6,8,9,[10,9,8,(88,99)])
# print(t5[4][3][1])
# # t5[4]=100#元组内元素不可修改，会报错
# #元组内元素不可修改，但可以修改元组内可变类型的元素,如列表等等
# t5[4][3]=1000
# print(t5)


# print(t1.index(11))#查元素索引是多少
# print(t1.count(11))#查元素出现的次数
# #max min sum len sorted函数同样适用于元组
#
# print(min(t1))#查最小值
# print(max(t1))#查最大值
# print(sum(t1))#查总和
# print(len(t1))#查长度

#sorted函数可以对元组进行排序,但返回元素类型都为列表
# print(sorted(t1,reverse=True),type(sorted(t1)))#进行排序，返回的类型为列表
# t1=tuple(sorted(t1))#将列表再转换为元组
# print(t1,type(t1))

# index=0
# while index<len(t1):
#     print(t1[index])
#     index+=1

# for item in t1:
#     print(item)
for index, item in enumerate(t2):
    print(index,item)
