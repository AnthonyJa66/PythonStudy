from collections import deque
#deque 是 Python 内置库 collections 中的一个数据结构，全称是 Double-Ended QUEue（双端队列）。

# 你可以把它理解成一个“两头都能高效进出”的列表。
dq = deque([1, 2, 3])

# 1. 从右边添加（默认）
dq.append(4)        # [1, 2, 3, 4]

# 2. 从左边添加
dq.appendleft(0)    # [0, 1, 2, 3, 4]

# 3. 从右边弹出
dq.pop()            # 返回 4，dq 变为 [0, 1, 2, 3]

# 4. 从左边弹出（这就是我之前用的）
dq.popleft()        # 返回 0，dq 变为 [1, 2, 3]