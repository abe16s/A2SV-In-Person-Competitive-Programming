# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        @cache
        def dp(mask, idx):
            if mask == (1<<n)-1:
                return 0
            
            cur = float("inf")
            for i in range(n):
                if not mask & (1<<i):
                    cur = min(cur, dp(mask|(1<<i), idx+1)+(nums1[idx] ^ nums2[i]))
            return cur
            
        return dp(0,0)
                    

