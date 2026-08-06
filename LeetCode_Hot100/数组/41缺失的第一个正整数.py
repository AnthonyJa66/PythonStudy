from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
          nums.append(0)
          n = len(nums)
        # answer = list(range(1, n + 2))
        # for item in answer:
        #
        #     if item not in nums:
        #         return item
        #
        # return -1







