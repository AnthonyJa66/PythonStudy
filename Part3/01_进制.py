#十进制

#二进制

#8进制

#16进制   0~9，A-F，满16进1


# # 0b开头表示二进制
# num1 = 0b11001  #1+0+0+2*2*2+2*2*2*2
# # 0o开头表示八进制
# num2 = 0o1034  #4+3*8+8*8*8
# # 0x开头表示十六进制
# num3 = 0x1cf #4+3*16+16*16
#
# print(f"二进制:0b11001={num1}",2**4+2**3+1)
# print(f"八进制:0o1034={num2}",4+3*8+8**3)
# print(f"十六进制:0x1cf={num3}",num3/16//16,num3//16%16,num3%16)
#
# print(0b101010)# 二进制  0b
# print(0o1111)#八进制 0o
# print(0x11f)#十六进制 0x   15+16+16*16=256+15+16

#注意：bin()、oct()、hex()返回的值类型都是字符串
a=bin(25)
print("bin()10进制转2进制",a,type(a))

c=oct(65)
print("oct()10进制转8进制",c,type(c))

b=hex(48)
print("hex()10进制转16进制",b,type(b))

#int(x,2/8/16)将其他进制转换回十进制,值类型也变成int
print(int(b,16),type(int(b,16)))
print(int(a,2),type(int(a,2)))

x=int('0b1111',2)
print(x)