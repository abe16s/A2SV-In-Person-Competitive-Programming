# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        bitset = bin(xor)[::-1].find("1") 
        shift = 1 << bitset
        cout = [0,0]
        for n in nums:
            if (n & shift):
                cout[0] ^= n
            else:
                cout[1] ^= n
        return cout