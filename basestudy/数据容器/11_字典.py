contacts = {"小明": "13800000000",
            "小红": "13900000000"}
print(contacts)

#查询指定键对应的值
print(contacts["小明"])


#添加键值对
contacts["小绿"]="13800000001"
contacts["小明"]="13800000002"

print(contacts)
#判断字典中是否存在指定键
print("小明"in contacts)

#删除指定键值对
del contacts["小明"]
print(contacts)


#查询字典中键值对的数量
print("字典中键值对的数量为:",len(contacts))


query=input("请输入要查询电话人员的姓名:")
if query in contacts:
    print(f'{query}的电话是:{contacts[query]}')
else:
    print(f"{query}不在通讯录中")
    print(len(contacts))
