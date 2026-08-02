#35搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。(也就是二分查找咯）
#
# 示例 1:
#
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
# 示例 2:
#
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
# 示例 3:
#
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
#
#
# 提示:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums 为 无重复元素 的 升序 排列数组
# -104 <= target <= 104



from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        #时间复杂度O(n)，容易超时，应该替换二分查找，并且插入位置威按顺序插入
        # if target in nums:
        #
        #     return nums.index(target)
        # else:
        #     nums.append(target)
        #     return len(nums)-1

        #二分查找，时间复杂度O(logn)
        left=0
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2

            if target<nums[mid]:
                right=mid-1
            elif target>nums[mid]:
                left=mid+1

            else:
                return mid
        #如果target不在nums中，返回left
        return left

