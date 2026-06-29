age = int(input("请输入年龄："))
has_report = input('你是否提交体检报告？是/否')
level = int(input("请输入会员等级（1/2/3）"))

if age >= 18 and age <= 45:
    print("年龄满足条件！")
    if has_report == '是':
        print("已提交体检报告！\n报名成功，可参加比赛")
        if level == 1:
            print(f'{level}级会员完成比赛可领取T恤👔一件')
        elif level == 2:
            print(f'{level}级会员完成比赛可领取跑步鞋👟')
        elif level == 3:
            print(f'{level}级会员完成比赛可领取耳机🎧')
        else:
            print('输入错误❌')
    else:
        print("未提交体检报告，报名失败")

else:
    print("抱歉，年龄不满足比赛条件")
