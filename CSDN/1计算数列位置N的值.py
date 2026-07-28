
m=int(input())
n=int(input())

list1=[]
for i in 1,m:
    list1.append(i)

if n in list1:
    print(min(list1)+max(list1))
elif n not in list1:
    print(max(list1)-1)

else:
    print("输入有问题")

