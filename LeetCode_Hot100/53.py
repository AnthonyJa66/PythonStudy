# 53.最大子数组和
# 中等
# 相关标签
# premium  lock  icon

# 给你一个整数数组
# nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。

# 示例 1：
# 输入：nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 输出：6
# 解释：连续子数组[4, -1, 2, 1]
# 的和最大，为6 。

# 示例2：
# 输入：nums = [1]
# 输出：1

# 示例3：输入：nums = [5, 4, -1, 7, 8]
# 输出：23

# 提示：
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

# 进阶：如果你已经实现复杂度为O(n)的解法，尝试使用更为精妙的分治法

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre=0
        maxsum=nums[0]
        for num in nums:
            pre=max(pre+num,num)
            maxsum=max(maxsum,pre)
        return maxsum

l=[5, 4, -1, 7, 8]

s=Solution()
print(s.maxSubArray(l))
