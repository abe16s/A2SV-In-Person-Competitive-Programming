# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        ctr = running = 0 
        dic[0] = 1
        for j in range(len(nums)):
            running += nums[j]
            key = running % k
            ctr += dic[key]
            dic[key] += 1
        return ctr