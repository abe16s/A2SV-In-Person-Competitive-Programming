# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapify(nums)
        score = 0
        for j in range(k):
            cur = -heappop(nums)
            score += cur
            heappush(nums, -ceil(cur/3))
        return score