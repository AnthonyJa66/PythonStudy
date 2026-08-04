"""128.最长连续序列
中等
给定一个未排序的整数数组nums找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为O(n)的算法解决此问题。

示例1：
输入：nums = [100, 4, 200, 1, 3, 2]
输出：4
解释：最长数字连续序列是[1, 2, 3, 4]。它的长度为4。

示例2：
输入：nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
输出：9

示例3：
输入：nums = [1, 0, 1, 2]
输出：3

提示：
0 <= nums.length <= 105
-109 <= nums[i] <= 109"""

from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m=len(nums)
        max_len=1
        num=sorted(nums)
        temp=0
        for i in range(m):
            if num[i]+1 not in num:
                temp=num[i+1]

            max_len=max(max_len,temp)


