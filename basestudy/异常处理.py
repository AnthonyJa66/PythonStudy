#当程序本身运行无问题，但因用户输入或者实际操作和程序预设不符导致程序无法运行的情况时有发生，
# 如：要求输入数字，用户输入字符串；
# 要求输入两个数字，用户输入多或少等等；

import sys  # 在文件开头导入 sys 模块

try:
    user_weight=float(input("请输入您的体重（单位kg）："))
    user_hight=float(input("请输入您的身高（单位m）："))
    user_BMI=user_weight/(user_hight*user_hight)
    if 50<user_BMI or user_BMI<10:
        print("你是外星人👽吗?")
        # sys.exit(0)  # 0 表示正常退出，程序立即终止
        sys.quit(0)
        # 注意：这里的 sys.exit() 会抛出 SystemExit 异常，但不会被 except 捕获（除非专门捕获）



except ValueError:#运行失败时输出，常写失败提示
    print("输入不为合理数字，请重新运行程序，并输入正确数字。")

except ZeroDivisionError:#输出值为0时，显示提示
    print("请输入不为0的值")

except:#产生所有错误导致不能运行时都可执行下方代码
    print("能不能老老实实看清规则使用！")



else:
    print(f'您的BMI是：{user_BMI}')

finally:
    print("程序执行完毕！")