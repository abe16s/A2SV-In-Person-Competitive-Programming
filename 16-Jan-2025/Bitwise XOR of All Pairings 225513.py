# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        ans = 0
        if n % 2:
            for i in range(m):
                ans ^= nums1[i]
        if m % 2:
            for j in range(n):
                ans ^= nums2[j]
        return ans