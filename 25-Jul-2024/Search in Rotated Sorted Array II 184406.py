# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue
            elif (nums[mid] < nums[l]) == (target < nums[l]):
                num = nums[mid]
            elif target < nums[l]:
                num = -float("inf")
            else:
                num = float("inf")

            if num < target:
                l = mid+1
            else:
                r = mid-1
        return False