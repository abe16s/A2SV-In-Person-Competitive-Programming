# Problem: Pacific Atlantic Water Flow - https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        flow = [[""]*n for _ in range(m)]
        #pacific
        queue = deque()
        for i in range(n):
            flow[0][i] = "p"
            queue.append([0,i])
        for i in range(1, m):
            queue.append([i,0])
            flow[i][0] = "p"

        nbrs = [(0,1), (0,-1), (-1,0), (1,0)]
        while queue:
            for _ in range(len(queue)):
                cur_r, cur_c = queue.popleft()
                for nbr_r, nbr_c in nbrs:
                    nbr_r += cur_r
                    nbr_c += cur_c
                    if 0 <= nbr_r < m and 0 <= nbr_c < n and flow[nbr_r][nbr_c] == "" and heights[nbr_r][nbr_c] >= heights[cur_r][cur_c]:
                        queue.append([nbr_r, nbr_c])
                        flow[nbr_r][nbr_c] = "p"

        #atlantic 
        queue = deque()
        for i in range(n):
            queue.append([m-1,i])
            flow[m-1][i] += "a"

        for i in range(m-1):
            queue.append([i,n-1])
            flow[i][n-1] += "a"

        while queue:
            for _ in range(len(queue)):
                cur_r, cur_c = queue.popleft()
                for nbr_r, nbr_c in nbrs:
                    nbr_r += cur_r
                    nbr_c += cur_c
                    if 0 <= nbr_r < m and 0 <= nbr_c < n and "a" not in flow[nbr_r][nbr_c] and heights[nbr_r][nbr_c] >= heights[cur_r][cur_c]:
                        queue.append([nbr_r, nbr_c])
                        flow[nbr_r][nbr_c] += "a"

        result = []
        for r in range(m):
            for c in range(n):
                if flow[r][c] == "pa":
                    result.append([r,c])
        return result