list = [1, 2, 3, 4, 5]
# print(list)
# print(type(list))
# print(len(list))
# print(list[0])

str=["hello","world","python"]
# print(str)
# print(type(str))
# print(str[0])
# print(len(str))

str.append("java")
# print(str)
str.insert(0,"python")
# print(str)
a=list+str
# print(a)
# print(type(a[5]))#列表可同时存储不同类型的元素

a.remove(1)#删除指定元素
print(a)

# a.clear()
# print(a)

# print(a[0:3])#切片操作

# print(a.sort())
# print(a.count())

# print(sorted(list),min(list),max(list))
# print(b=sorted(list,reverse=True))
b=sorted(list,reverse=True)
# print(b,min(b))
# print(list)
a.remove('python')
print(b)
print(a)

