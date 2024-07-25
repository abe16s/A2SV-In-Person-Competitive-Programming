# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = set()
        rows = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)
        for r in rows:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0
        for c in cols:
            for j in range(len(matrix)):
                matrix[j][c] = 0
