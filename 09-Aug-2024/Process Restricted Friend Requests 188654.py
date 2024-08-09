# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
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
                    p, c = parentX, parentY
                elif rank[parentX] < rank[parentY]:
                    parent[parentX] = parentY
                    p, c = parentY, parentX
                else:
                    parent[parentX] = parentY
                    rank[parentY] += 1
                    p, c = parentY, parentX
                friends[p].update(friends[c])
        
        parent = [i for i in range(n)]
        friends = [{i} for i in range(n)] 
        rank = [0] * n

        restrictions = {tuple(i) for i in restrictions}

        result = []
        for u, v in requests:
            successful = True
            for f in friends[find(u)]:
                for ind_f in friends[find(v)]:
                    if (f,ind_f) in restrictions or (ind_f,f) in restrictions:
                        successful = False
                        break
                if not successful:
                    break 

            if successful:
                union(u,v)
            result.append(successful)
        
        return result