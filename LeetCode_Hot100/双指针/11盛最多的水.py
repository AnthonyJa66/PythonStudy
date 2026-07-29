# 11盛最多的水

# 示例1：
# 输入：[1, 8, 6, 2, 5, 4, 8, 3, 7]
# 输出：49
# 解释：图中垂直线代表输入数组[1, 8, 6, 2, 5, 4, 8, 3, 7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为
# 49。
#
# 示例2：
# 输入：height = [1, 1]
# 输出：1
#
# 提示：
#
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area=0

        #暴力解法时间复杂度O(n**2)，容易超时
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         area=(j-i)*min(height[i],height[j])
        #         max_area=max(max_area,area)
        # return max_area

        #双指针 时间复杂度O(n)
        left,right=0,len(height)-1
        while left<right:
            cur_area=(right-left)*min(height[left],height[right])
            max_area=max(cur_area,max_area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return max_area








