# Problem: Build a Matrix With Conditions - https://leetcode.com/problems/build-a-matrix-with-conditions/

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for a, b in rowConditions:
            graph[a].append(b)
            indegree[b] += 1

        queue = deque()
        for n in range(1, k+1):
            if not indegree[n]:
                indegree.pop(n)
                queue.append(n)
        
        rows = [0] * n
        r = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                rows[cur-1] = r
                r += 1
                for nbr in graph[cur]:
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0:
                        queue.append(nbr)
                        indegree.pop(nbr)

        if indegree:
            return []


        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for l, r in colConditions:
            graph[l].append(r)
            indegree[r] += 1

        queue = deque()
        for n in range(1, k+1):
            if not indegree[n]:
                indegree.pop(n)
                queue.append(n)
        
        cols = [0] * n
        c = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                cols[cur-1] = c
                c += 1
                for nbr in graph[cur]:
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0:
                        queue.append(nbr)
                        indegree.pop(nbr)
        if indegree:
            return []

        matrix = [[0]*k for _ in range(k)]
        for n in range(k):
            matrix[rows[n]][cols[n]] = n+1

        return matrix