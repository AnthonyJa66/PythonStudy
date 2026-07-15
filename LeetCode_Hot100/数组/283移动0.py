from typing import List  # 需要加这行

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # a = len(nums)
        # b = []
        # c = []
        # for i in range(a):
        #     if nums[i] == 0:
        #         b.append(0)
        #     else:
        #         c.append(nums[i])
        # nums[:] = c + b
        #= 是重新绑定标签，[:] 是修改对象内容。在顶层用 = 没问题；在函数内想修改调用者的列表，必须用 [:]。

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


nums=[0,0,1,0,3,12]
s=Solution()

s.moveZeroes(nums)
print(nums)

# list1=[0,1,0,3,12]
# list2=[0,1,0,3,12]
# list3=list1+list2
# print(list3)
