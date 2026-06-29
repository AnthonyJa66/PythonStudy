
print("请输入学生成绩，输入“结束”停止录入")

score_list=[]
while 1:
    score=input("请输入成绩：")
    if score=="结束":
        break
    else:
        score_list.append(int(score))

if score_list:
    print("总人数为：",len(score_list))
    avg=sum(score_list)/len(score_list)
    print(f"平均分数为：{avg:.2f}")
    pass_cout=0
    ex_cout=0
    for index in range(len(score_list)):
        if score_list[index]>60:
            pass_cout+=1
            if score_list[index]>=90:
                ex_cout+=1
    print(f"及格人数为：{pass_cout}")
    print(f"优秀人数为：{ex_cout}")
    print(f'合格率为：{pass_cout/len(score_list)*100:.2f%}')
    print(f'优秀率为：{ex_cout/len(score_list)*100:.2f%}')
    print(f'最高成绩为：{max(score_list)}')
    print(f'最低成绩为：{min(score_list)}')
else:
    print("没有录入成绩")

