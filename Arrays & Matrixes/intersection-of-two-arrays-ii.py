class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j =  0
        output = []
        while i < len(nums1):
            a = 1
            cur = nums1[i]
            while i+1 < len(nums1) and nums1[i+1] == nums1[i]:
                a += 1
                i += 1
            b = 0
            while j < len(nums2) and nums2[j] <= cur:
                if nums2[j] == cur:
                    b += 1
                j += 1
            output.extend([cur]*min(a,b))
            i += 1
        return output
