# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
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
                seg_sum[p] += seg_sum[c]

        n = len(nums)
        parent = [i for i in range(n)]
        rank = [1] * n
        seg_sum = [nums[_] for _ in range(n)]
        maxi = 0
        cout = []
        found = set()
        for i in range(n-1, -1, -1):
            cout.append(maxi)
            cur = removeQueries[i]
            if cur-1 in found:
                union(cur-1, cur)
            if cur+1 in found:
                union(cur+1, cur)
            found.add(cur)
            maxi = max(maxi, seg_sum[find(cur)])

        return cout[::-1]