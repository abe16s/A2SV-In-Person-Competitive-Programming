class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] >= target:
                r = mid-1
            else:
                l = mid+1
        if l >= len(nums) or nums[l] != target:
            return [-1,-1]
        ans = [l, l]
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        ans[1] = r
        return ans