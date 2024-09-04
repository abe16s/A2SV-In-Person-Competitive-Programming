# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = ""
        for c in s:
            nums += str(ord(c)-96)
        
        for i in range(k):
            nums = str(sum(map(int, nums)))
        
        return int(nums)