import sys
num=300000

price=50_000_000#为了方便程序员数清数字，可以穿插下划线，不影响整形数字大小

print(num)
print(price)

a=9**9999
sys.set_int_max_str_digits(0)#调用sys模块，解除整形位数限制


print(a)#python能打印的整形大小取决于计算机的性能，规范上没限制