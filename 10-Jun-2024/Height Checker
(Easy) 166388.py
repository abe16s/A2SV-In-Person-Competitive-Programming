# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * (max(heights)+1)
        for h in heights:
            count[h] += 1
        
        expected = 0
        ctr = 0
        for c in range(len(count)):
            for k in range(count[c]):
                if heights[expected] != c:
                    ctr += 1
                expected += 1
        return ctr

        
        