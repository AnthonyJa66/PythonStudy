from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        target_list=[]
        while 1:
            for j in range(n):
                target_list.append(matrix[0][j])
                m-=1
            for i in range(1, n):
                target_list.append(matrix[i][m])
            for i in range(m, 1, -1):
                target_list.append(matrix[i][n - 1])
            for j in range(n - 2, 0, -1):
                target_list.append(matrix[0][j])




