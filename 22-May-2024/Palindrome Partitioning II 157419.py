# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        def check_palindrom(ss):
            return ss == ss[::-1]

        @cache
        def dp(cur):
            if check_palindrom(cur):
                return 0
            
            mini = len(cur)-1
            for i in range(1, len(cur)):
                if check_palindrom(cur[:i]):
                    mini = min(dp(cur[i:])+1, mini)
            return mini
        
        return dp(s)