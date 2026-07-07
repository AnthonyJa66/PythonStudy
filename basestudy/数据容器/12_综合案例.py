name_list = ["小明", "小绿", "小红", "小蓝", "小w"]

dic = {"小明": "鸡",
       "小红": "兔",
       "小绿": "龙",
       "小蓝": "虎",
       "小紫": "蛇",
       "小wang": "龙",
       "anthony": "龙",
       }
print(dic[name_list[0]])
for i in range (len(name_list)):
    if name_list[i] in dic:
        print(f"{name_list[i]}生肖是{dic[name_list[i]]}")
    else:
        print(f"{name_list[i]}无信息")
