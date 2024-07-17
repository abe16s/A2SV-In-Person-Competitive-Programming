# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ps = [[0]*(n+1)]
        for r in range(m):
            ps.append([0])
            for c in range(n):
                ps[-1].append(mat[r][c])
        for i in range(1, m+1):
            for j in range(1, n+1):
                ps[i][j] += ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]
        
        ans = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                rs, re, cs, ce = max(r-k, 0), min(r+k+1, m), max(c-k, 0), min(c+k+1, n)
                ans[r][c] = ps[re][ce] + ps[rs][cs] - ps[rs][ce] - ps[re][cs]
        return ans

