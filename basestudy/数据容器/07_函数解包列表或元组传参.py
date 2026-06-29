# 定义函数时，使用*args（变量不一定非要用args，比如写：*data也行），将收到的多个参数，打包成一个元组
def test(*data):
    print(f'参数为：{data}，参数类型是：{type(data)}')

list1=[1,2,3,4,5]
tuple1=(1,2,3,"hello",5)

test(list1)
test(tuple1)

test(*list1)#解包列表，将列表每个元素拆分传入，相当于传入了1,2,3,4,5
test(*tuple1)#解包元组，将元组每个元素拆分传入，相当于传入了1,2,3,4,5
