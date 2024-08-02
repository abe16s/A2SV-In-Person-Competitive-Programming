# Problem: 4Sum - https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        cout = []
        for j in range(len(nums)-3): 
            if j and nums[j] == nums[j-1]:
                continue
            for i in range(j+1, len(nums)-2):
                if i != j+1 and nums[i] == nums[i-1]:
                    continue
                temp = target - nums[i] - nums[j]
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == temp:
                        cout.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < len(nums) and nums[l] == nums[l-1]:
                            l += 1
                    elif nums[l] + nums[r] < temp:
                        l += 1
                    else:
                        r -= 1
        return cout