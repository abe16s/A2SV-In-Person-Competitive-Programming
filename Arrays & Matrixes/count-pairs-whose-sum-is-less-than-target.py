class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        ctr = 0
        print(nums)
        for i in range(len(nums)):
            cur = target
            j = i + 1 
            while cur <= target and  j < len(nums):
                cur = nums[i] + nums[j]
                if cur < target:
                    ctr += 1
                j += 1
        return ctr
