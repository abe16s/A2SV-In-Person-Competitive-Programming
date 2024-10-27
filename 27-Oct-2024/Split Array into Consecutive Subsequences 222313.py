# Problem: Split Array into Consecutive Subsequences - https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        tails = defaultdict(list)

        for n in nums:
            if tails[n - 1]:
                length = heappop(tails[n - 1]) + 1
                heappush(tails[n], length)
            else:
                heappush(tails[n], 1)
    
        for tail in tails.values():
            for l in tail:
                if l < 3:
                    return False
        
        return True
                                          
        