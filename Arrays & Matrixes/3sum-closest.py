class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mini = float("inf")
        nums.sort()
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                summ = nums[i]+nums[j]+nums[k]
                if summ == target:
                    return summ
                elif summ < target:
                    j += 1
                else:
                    k -= 1
                if abs(target-summ) < abs(mini-target):
                    mini = summ
        return mini