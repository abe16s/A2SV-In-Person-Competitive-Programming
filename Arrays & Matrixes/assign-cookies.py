class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)
        ctr = 0
        i = 0
        for cookie in s:
            while i < len(g) and g[i] > cookie:
                i += 1
            if i < len(g):
                i += 1
                ctr += 1 
        return ctr