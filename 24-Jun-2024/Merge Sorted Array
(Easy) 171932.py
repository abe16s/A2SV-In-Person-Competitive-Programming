# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        n1 = n2 = i = 0
        while n1 < m and n2 < n:
            if temp[n1] < nums2[n2]:
                nums1[i] = temp[n1]
                n1+=1
            else:
                nums1[i] = nums2[n2]
                n2+=1
            i+=1
        if n1 < m:
            nums1[i:] = temp[n1:]
        if n2 < n:
            nums1[i:] = nums2[n2:]
