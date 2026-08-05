# 56合并区间
#以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

# 示例 1：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

# 示例 2：
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

# 示例 3：
# 输入：intervals = [[4,7],[1,4]]
# 输出：[[1,7]]
# 解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。

# 提示：
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104


from typing import List
from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # n=len(intervals)
        intervals.sort()
        res=[]
        queue = deque(intervals)
        a=queue.popleft()

        if len(intervals)<2:
            return intervals
        # while queue:
        #     cur=queue.popleft()
        #     if cur[0]<=a[1]:
        #         a[1]=cur[1]
        #     else:
        #         res.append(a)
        #         a=cur

        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] <= a[1]:
                a[1] = max(a[1], cur[1])
            else:
                res.append(a)
                a = cur
            if i == len(intervals) - 1:
                res.append(a)
        return res




s=Solution()
intervals=[[1,3],[2,6],[8,10],[15,18],[1,4],[2,9]]
r=s.merge(intervals)
print(r)

