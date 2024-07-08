# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        offset = 0
        ans = 0
        happiness.sort(reverse=True)
        for i in range(k):
            cur = happiness[i]
            ans += max(cur-offset, 0)
            offset += 1
        return ans
