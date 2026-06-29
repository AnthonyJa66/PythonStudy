def greet(name,msg):
    print(f'我叫{name},',end='')
    speak(msg)

def speak(msg):
    # print('hello')
    print(msg)


greet("张三","你好")




# 函数嵌套调用测试2
#函数内按顺序执行完毕
def test1():
    print('进入 test1 函数')
    test2()
    print('退出 test1 函数')#暂存待执行1，先进后出——栈

def test2():
    print('进入 test2 函数')
    test3()
    print('退出 test2 函数')#暂存待执行2，先进后出——栈

def test3():
    print('进入 test3 函数')
    print('***正在执行 test3 函数')
    print('退出 test3 函数')

test1()