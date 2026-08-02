#74搜索二维矩阵
#给你一个满足下述两条属性的 m x n 整数矩阵：
# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
#
# 你必须编写一个时间复杂度为 O(log(m * n)) 的解决方案。
#
# 示例 1：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true

# 示例 2：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
#
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #先将二维数组转换为一维数组，可返回正确，但时间复杂度O(m x n)，容易超时

        # n = len(matrix)
        # list1=[]
        # for i in range(n):
        #     list1.append(matrix[i])
        # left=0
        # right=len(list1)-1
        # while left<=right:
        #     mid=(left+right)//2
        #
        #     if list1[mid]>target:
        #         right=mid-1
        #     elif list1[mid]<target:
        #         left=mid+1
        #     else:
        #         return True
        # return False

        #二分查找 时间复杂度O(log(m * n))
        n=len(matrix)
        m=len(matrix[0])
        left=0
        right=n*m-1
        while left<=right:
            mid = (left+right)//2
            if matrix[mid//m][mid%n]>target:
                right=mid+1
            elif matrix[mid//m][mid%n]<target:
                left=mid+1
            else:
                return True
        return False
