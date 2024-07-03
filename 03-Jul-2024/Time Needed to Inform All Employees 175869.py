# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for e, m in enumerate(manager):
            if m != -1:
                graph[m].append(e)
        queue = deque([headID])
        minutes = 0
        while queue:
            cur = queue.popleft()
            minutes = max(minutes, informTime[cur])
            for nbr in graph[cur]:
                queue.append(nbr)
                informTime[nbr] += informTime[cur]
        return minutes

