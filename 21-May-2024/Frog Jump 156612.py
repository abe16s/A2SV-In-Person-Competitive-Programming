# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        last = stones[-1]
        stones_set = set(stones)
        @cache
        def dp(cur, jump):
            if cur not in stones_set or jump == 0:
                return False
            
            if cur == last:
                return True
            
            return dp(cur+jump-1, jump-1) or dp(cur+jump, jump) or dp(cur+jump+1, jump+1)
        
        return dp(1, 1)