list2=[2,"中国建设银行","中国工商银行",4,5,"中国建设银行","中国工商银行"]

# #列表.index方法查询指定元素的索引位置
# print(list2.index("中国建设银行"))#查找元素不存在会报错
#
# #列表.count方法查询指定元素出现的次数
# print(list2.count("中国建设银行"))

list3=[5,7,1,3,5,[1,5,2,10]]
# print(list3.index(5))#查找元素不存在会报错
# print(list3.count(1))

list3.pop(5)
print(list3)
#列表.sort方法对列表进行排序,reverse=True表示降序排序,reverse=False表示升序排序
list3.sort(reverse=True)#无返回值
print(list3)

# #列表.reverse方法对列表进行反转
print(list2)
list2.reverse()#无返回值
print(list2)


