# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a = edges[0][0]
        b = edges[0][1]
        if a in edges[1]:
            return a
        if b in edges[1]:
            return b