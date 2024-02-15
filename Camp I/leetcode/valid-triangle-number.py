class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        valid = 0
        i = 0
        for i in range(len(nums)-2):
            ctr = 0
            r = len(nums) - 1
            for l in range(i+1, len(nums)-1):
                while r > l and nums[r] + nums[l] <= nums[i]:
                    r -= 1
                if r < l:
                    r += 1
                ctr += r-l
            valid += ctr
        return valid