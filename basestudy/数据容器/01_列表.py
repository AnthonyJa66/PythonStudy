nums=[1,2,3,4,5,6,7,8,9,10]

# print(sorted(nums,reverse=True))

list1=["神剑股份","中国银行","中国建设银行","中国农业银行","中国交通银行",54,545,[1,5,6,8,5212]]

#增删改查 create read update delete

#增 append方法增加到列表最后
#insert方法添加到指定位置
#extend方法扩展列表
list1.append("中银")#append方法增加到列表最后
list1.insert(2,"中国工商银行")#insert方法添加到指定位置

a=[20,5,"上位机"]
list1.extend(a)
print(list1)

#删 remove方法删除指定元素
#pop方法删除指定位置元素
#clear方法清空列表

# list1.remove("中银")#remove方法删除第一次出现的指定元素
# print(list1)
#list1.pop(2)##pop方法删除指定位置元素，pop方法有返回值，其他删除方法没有返回值
# print(list1.pop(2))#返回值为删除元素
# list1.clear()#clear方法清空列表
# print(list1)
#通过del关键字删除指定位置元素
# del list1[2]
# print(list1)

#修改 修改指定位置元素的值
list1[2]="中国建设银行"
print(list1)

#查询 查询指定位置元素的值 
print(list1[2])
print(list1[2][0])
print(list1[2][0:3])
