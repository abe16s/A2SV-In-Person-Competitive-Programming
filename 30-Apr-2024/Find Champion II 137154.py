# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = defaultdict(int)
        for a, b in edges:
            indegree[b] += 1
        cout = []
        for i in range(n):
            if indegree[i] == 0:
                cout.append(i)
        return cout[0] if len(cout) == 1 else -1 