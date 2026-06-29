for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')#默认end="\n"换行
    print('')#起换行作用，如果是\n则换两行
