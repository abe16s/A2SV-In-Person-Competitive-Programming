# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = {}
        possible_palindroms = []

        def check_palindrom(ss):
            if ss == "":
                return False
            l, r = 0, len(ss)-1
            while l <= r:
                if ss[l]!=ss[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dp(start_idx, cur_idx, palindroms):
            if cur_idx == len(s):
                if start_idx == cur_idx:
                    possible_palindroms.append(palindroms[:])
            if cur_idx > len(s):
                return
            
            dp(start_idx, cur_idx+1, palindroms)
            if check_palindrom(s[start_idx:cur_idx]):
                palindroms.append(s[start_idx:cur_idx])
                dp(cur_idx, cur_idx, palindroms)
                palindroms.pop()
        
        dp(0,0,[])
        return possible_palindroms