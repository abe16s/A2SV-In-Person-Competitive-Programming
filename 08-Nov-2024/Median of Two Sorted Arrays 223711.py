# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)

        total = n1 + n2
        target = (total+1)//2
        l, r = 0, n1
        while True:
            take1 = l + (r-l)//2
            take2 = target-take1
            
            max1 = nums1[take1-1] if take1 > 0 else -float("inf")
            min1 = nums1[take1] if take1 < n1 else float("inf")
            max2 = nums2[take2-1] if take2 > 0 else -float("inf")
            min2 = nums2[take2] if take2 < n2 else float("inf")

            if max1 > min2:
                r = take1-1
            elif max2 > min1:
                l = take1+1
            else:
                medianValOdd = max(max1, max2)
                if total % 2:
                    return medianValOdd
                else:
                    return (medianValOdd + min(min1, min2)) / 2