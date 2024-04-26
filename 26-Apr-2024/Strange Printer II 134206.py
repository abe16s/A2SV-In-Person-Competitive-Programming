# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m = len(targetGrid)
        n = len(targetGrid[0])
        bound = {} #start row, start col, end row, end col 

        for i in range(m):
            for j in range(n):
                if targetGrid[i][j] not in bound:
                    bound[targetGrid[i][j]] = [i,j,i,j]
                else:
                    sr, sc, er, ec = bound[targetGrid[i][j]]
                    bound[targetGrid[i][j]] = [min(sr,i), min(sc,j), max(er,i), max(ec,j)]

        indegree = defaultdict(int)
        nbrs = defaultdict(set)

        for i in range(m):
            for j in range(n):
                for k in bound:
                    if targetGrid[i][j] != k:
                        sr, sc, er, ec = bound[k]
                        if sr <= i <= er and sc <= j <= ec:
                            if targetGrid[i][j] not in nbrs[k]:
                                indegree[targetGrid[i][j]] += 1
                                nbrs[k].add(targetGrid[i][j])
        queue = deque()
        for k in bound:
            if indegree[k] == 0:
                queue.append(k)
            
        topsort = []
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                topsort.append(cur)
                for nbr in nbrs[cur]:
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0:
                        queue.append(nbr)

        return len(topsort) == len(bound)
                     
