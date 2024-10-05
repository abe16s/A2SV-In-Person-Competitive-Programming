# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = defaultdict(int)
        for n in arr:
            remainder[n%k] += 1
        if remainder[0] % 2 != 0:
            return False
        for i in range(1, k):
            if remainder[i] != remainder[k-i]:
                return False
        return True