import os


# f=open("D:\\workspace\\OpenCodeProjects\\PythonStudy\\1.txt","r",encoding="utf-8")#r表示只读模式打开文件,w表示写入模式打开文件，a表示追加模式打开文件，b表示二进制模式打开文件
# f1=open("../../1.txt","r",encoding="utf-8")#r表示只读模式打开文件,w表示写入模式打开文件，a表示追加模式打开文件，b表示二进制模式打开文件

# # print(f1.read())
# # print(f1.readline()+f1.readline())
# print(f1.readlines())
# f1.close()#需要关闭文件,释放资源


f="../../1.txt"
#
# #with open()语句：自动关闭文件,释放资源
# with open("D:/workspace/OpenCodeProjects/PythonStudy/1.txt", encoding="utf-8") as fileload:
#     print(fileload.read())

file_address="../../成绩.xls"
# with open(file_address,"w",encoding="utf-8") as f2:
#     #w模式会覆盖文件原有内容
#     f2.write("hello world\n")
#     f2.write(" world")

# with open(file_address,"a",encoding="utf-8") as f3:
#     #a模式会追加文件原有内容
#     f3.write("\nhello world\n")

with open(file_address,"r+",encoding="utf-8") as f4:
    #r+模式会先读取文件内容，再写入文件内容
#可以调用read()函数读取文件内容，也可以调用write()函数写入文件内容
    print(f4.read())
    f4.write("h\n")
    print("写入后文件内容为："+f4.read())#注意read()函数会从当前位置开始读取，所以需要先调用seek()函数将当前位置移动到文件开头，才能读取到文件内容
    f4.seek(0)
    print(f4.read())