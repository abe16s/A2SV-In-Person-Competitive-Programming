# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums)-1:
            if nums[i] + i >= len(nums)-1:
                return True
            if not nums[i]:
                return False
            nxt = i + 1
            for j in range(1, nums[i]+1):
                if i+j + nums[i+j] > nxt + nums[nxt]:
                    nxt = i+j
                j += 1
            i = nxt
        return True
