# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                if rank[parentX] > rank[parentY]:
                    parent[parentY] = parentX
                elif rank[parentX] < rank[parentY]:
                    parent[parentX] = parentY
                else:
                    parent[parentX] = parentY
                    rank[parentY] += 1

        parent = [i for i in range(n)]
        rank = [1] * n
        secrets = {0}
        meetings.append([0, firstPerson,0])
        meetings.sort(key=lambda x: x[2])
        # for a, b, time in meetings:
        #     if a in secrets or b in secrets:
        #         union(a,b)
        #         secrets.add(a)
        #         secrets.add(b)
        m = 0
        while m < len(meetings):
            time = meetings[m][2]
            cur = []
            while m < len(meetings) and meetings[m][2] == time:
                cur.append(meetings[m])
                m += 1

            for x, y, t in cur:
                union(x,y)
            
            for x, y, t in cur:
                p = find(x)
                if p != find(0):
                    parent[x] = x
                    parent[y] = y
                else:
                    secrets.add(x)
                    secrets.add(y)

        return secrets
