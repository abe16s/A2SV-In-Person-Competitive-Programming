class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones_right = nums.count(1)
        zeros_right = nums.count(0)
        ones_left = 0
        zeros_left = 0
        max_idx = {0}
        max_score = ones_right
        for i in range(1, len(nums)+1):
            if nums[i-1] == 0:
                zeros_left += 1
                zeros_right -= 1
            elif nums[i-1] == 1:
                ones_left += 1
                ones_right -= 1
            cur = zeros_left + ones_right
            if cur > max_score:
                max_idx = {i}
                max_score = cur
            elif cur == max_score:
                max_idx.add(i)

        return list(max_idx)