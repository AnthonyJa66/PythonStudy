from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # for i in range(m):
        #     for j in range(n):
        #         for a,b in lis:
        #             matrix[a][j]=0
        #             matrix[i][b]=0
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0

        return matrix


mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
s = Solution()

print(s.setZeroes(mat))
