# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        cout = [0] * len(nums)
        maxi = 2**maximumBit - 1 
        for i in range(len(nums)):
            xor ^= nums[i]
            cout[len(nums)-i-1] = maxi - xor
        
        return cout