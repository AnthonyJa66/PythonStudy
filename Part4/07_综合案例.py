print('Game Start')

# question

# 使用嵌套列表来存储，外层列表包含多个内层列表
q = [
    ['Python输出函数是什么？', 'print'],
    ['Python中表示逻辑并且的关键字是？', 'and'],
    ['Python属于编译型还是解释型？', '解释型']
]

# print(q[0][0])
# 方案二：用字典（键值对），非常适合问答数据
qa_dict = {
    'Python输出函数是什么？': 'print',
    'Python中表示逻辑并且的关键字是？': 'and',
    'Python属于编译型还是解释型？': '解释型'
}

# print(qa_dict['Python输出函数是什么？'])  # 直接通过问题拿答案

ques1, ans1 = 'Python输出函数是什么？', 'print'
ques2, ans2 = 'Python中表示逻辑并且的关键字是？', 'and'
ques3, ans3 = 'Python属于编译型还是解释型？', '解释型'

max_chances = 3

toral_levels = 3

is_playing = True

tries = 1
for level in range(1, toral_levels + 1):

    # if level == 1:
    #     question, answer = ques1, ans1
    # elif level == 2:
    #     question, answer = ques2, ans2
    # elif level == 3:
    #     question, answer = ques3, ans3

    question = q[level - 1][0]
    answer = q[level - 1][1]


    print(f'第{level}关')
    while tries <= max_chances:
        ans = input(f'{question},你的回答是：')
        if ans == "":
            print('你的回答是空，请重新作答！')
            continue
        elif ans == answer:
            print(f'第{level}关回答正确\n')
            break
        else:
            leave = max_chances - tries
            if leave > 0:
                print(f'回答错误，还有{leave}次机会，请继续尝试')
                tries += 1
                continue
            else:
                print(f'闯关失败，正确答案{answer}')
                is_playing = False
                break
    if not is_playing:
        break
if is_playing:
    print('成功！')
