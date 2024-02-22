class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ctr = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
               bucket = math.ceil(nums[i]/nums[i+1])
               nums[i] = nums[i] // bucket
               ctr += bucket - 1
        return ctr
        

        