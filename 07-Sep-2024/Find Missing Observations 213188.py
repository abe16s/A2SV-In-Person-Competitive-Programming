# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_n = mean * (n+len(rolls)) - sum(rolls) 
        ns = []
        for i in range(n):
            x = sum_n // (n-i)
            if x > 6 or x <= 0:
                return []
            ns.append(x)
            sum_n -= ns[-1]
        return ns