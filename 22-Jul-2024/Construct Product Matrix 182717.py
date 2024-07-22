# Problem: Construct Product Matrix - https://leetcode.com/problems/construct-product-matrix/description/

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        pre = [[1] * (m) for _ in range(n)]
        suf = [[1] * (m) for _ in range(n)]
        rp = 1 
        sp = 1
        for r in range(n):
            for c in range(m):
                pre[r][c] = rp
                rp = rp * grid[r][c] % 12345

                suf[n-r-1][m-c-1] = sp
                sp = sp * grid[n-r-1][m-c-1] % 12345

        for r in range(n):
            for c in range(m):
                grid[r][c] = pre[r][c] * suf[r][c] % 12345
        return grid