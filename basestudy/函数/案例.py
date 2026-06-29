# sum=0
# def sumf(n):
#     global sum
#     sum += n
#     return sum
#
# print("7天俯卧撑统计")
# for i in range(1,8):
#     n = int(input(f"第{i}天："))
#     sumf(n)
#
# print("7天的总和为：",sum,"平均数为：",int(sum/7))
from fontTools.misc.cython import returns
from numpy.ma.extras import average


# def add_to_total(current_total, n):
#     return current_total + n
#
# total = 0
# print("7天俯卧撑统计")
# for i in range(1, 8):
#     n = int(input(f"第{i}天："))
#     total = add_to_total(total, n)
#
# print("7天的总和为：", total)


def calc_total(*nums):
    """
    计算俯卧撑的总和和平均数
    :param nums: 俯卧撑的次数
    :return: 总和和平均数
    """
    # print(nums)
    return sum(nums)

def calc_avg(total,days=7):
    """
    计算俯卧撑的平均数
    :param total: 总和
    :param days: 天数
    :return: 平均数
    """
    return (total/days)

def check_success(total,goal=120):
    """
    检查是否完成目标
    :param total: 总和
    :param goal: 目标值
    :return: 完成目标的提示
    """
    if total>goal:
        return f"恭喜你，成功完成{goal}次目标！"
    else:
        return f"很遗憾，没有完成{goal}次目标。"

def main(title,duration,goal):
    """
    主函数
    :param title: 运动名称
    :param duration: 天数
    :param goal: 目标值
    :return:
    """
    print(f'{title}{duration}天挑战赛（请输入每天的运动数量）')
    nums=[]

    for i in range(1,duration+1):
        nums.insert(i-1,int(input(f"请输入第{i}天的运动数量：")))#列表收集数据并进行处理
    #嵌套调用函数
    total=calc_total(*nums)

    avg=calc_avg(total,duration)

    result=check_success(total,goal)

    print(f"总和为：{total}，平均数为：{avg:.1f}")
    print(result)

main("引体向上",3,30)
