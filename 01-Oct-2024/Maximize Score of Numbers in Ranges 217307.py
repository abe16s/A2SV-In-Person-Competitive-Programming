# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        def check(cur):
            last_chosen_value = start[0]
            for i in range(1, len(start)):
                if last_chosen_value + cur > start[i] + d:
                    return False
                last_chosen_value = max(last_chosen_value + cur, start[i])
            return True

        l = 0
        r = start[-1]+d - start[0]
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return l-1