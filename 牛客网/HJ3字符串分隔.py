import sys

s = input()

list1 = list(s)
l = len(list1)
q = (l % 8)
temp = []
for i in range(l):
    temp.append(list1[i])

    if (i + 1) % 8 == 0:
        print(''.join(temp))
        temp = []

if q != 0:
    for _ in range(8 - l % 8):
        temp.append('0')

print(''.join(temp))

s = sys.stdin.readline().strip()
# sys.stdin.readline().strip()：比 input()更快，
# strip()用于去除输入末尾的换行符\n，避免它被当作一个字符处理。

print(s)
char_map = {}
