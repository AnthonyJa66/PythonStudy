##while循环
# print("正确回答问题，挑战成功")
# riddle = '你是什么人？'
# answer = '你的心上人'
# guess = ''
#
# while guess != answer:
#     print(f'问题：{riddle}')
#     guess = input('请输入答案：')
#     if guess == answer:
#         print("successful")
#     else:
#         print("unsuccessful")

# for循环

# for n in range(1 , 10):
#     print(f"第{n}次打印")
#
# print(n)#不建议在循环外部调用循环变量

# for m in 'abc有嘎嘎defghijklmn':#for循环也可直接打印字符串中每个最小元素
#     print(m)

# nums=[1,5,6,8,9]
# # for num in nums:#for循环也可直接调用列表中元素
# #     print(num)
#
# #死循环展示：
# for num in nums:
#     #nums.append(6)#不建议在for循环内部修改变量，容易死循环或中断
#     print(num)

#加密解密文字

text = input('请输出需要加密的文字：')
secrect = ''
for t in text:
    unicode = ord(t)  # ord()函数将值转为Unicode编码
    #print(unicode)
    secrect += chr(unicode + 1)  # chr()函数将值转为字符编码
print(f'{secrect}')

secr = input('请输出需要解密的文字：')
an=''
for s in secr:
    an += chr(ord(s) - 1)
print(f'{an}')