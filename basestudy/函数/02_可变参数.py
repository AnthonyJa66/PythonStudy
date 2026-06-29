#可变位置参数
# args只是形参名，可以随意更改，存放函数调用时传入的所有位置参数实参，
# args的数据类型是元组，args指的是arguments 参数
def test(*args):
    print(args)

# test("张三",18,"男","2023001")

#可变关键字参数
# kwargs只是形参名，可以随意更改，存放函数调用时传入的所有关键字参数实参，
# kwargs的数据类型是字典，kwargs指的是keyword arguments 关键字参数
# 形参前加**，代表可接收任意数量的关键字参数，并打包成一个字典
def test1(**kwargs):
    print(kwargs)

test1(c="9",age=18,gender="男",id="2023001")



#所有参数类型都可在函数中混用
def test2(name,*args,c="",**kwargs):
    print(name,args,c,kwargs)

test2("张三",18,c="9",age=18,gender="男",id="2023001")

