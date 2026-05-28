# for嵌套循环实现打印训练计划

for day in range(1, 8):
    print(f'这是第{day}天训练')
    for group in range(1, 4):
        if day%2 ==1 and group%2 == 0:
            print(f'这是第{day}天，第{group}组训练未完成')
        else:
            print(f'这是第{day}天，第{group}组训练')
