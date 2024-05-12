# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = []
        for i in range(n-2):
            cur = []
            for j in range(n-2):
                maxi = 0
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        maxi = max(maxi,grid[r][c])
                cur.append(maxi)
            maxLocal.append(cur)
        return maxLocal

