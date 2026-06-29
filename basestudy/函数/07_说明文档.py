def add(n1, n2):
    """函数说明文档
    计算两个数相加的结果
    :param 表示参数 n1:第一个数
    :param n2:第二个数
    :return:表示返回值 二者相加的结果
    """
    return n1 + n2

result = add(1, 2)

def factorial(n):
    #函数声明文档
    """
    计算n的阶乘是多少
    :param n:
    :return: n的阶乘结果
    """
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


factorial(5)
