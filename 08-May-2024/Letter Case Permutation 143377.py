# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        seen = set() 
        for i in range(2 ** n):
            temp = ""
            for j in range(n):
                if (i >> j) & 1:
                    temp += s[j].upper()
                else:
                    temp += s[j].lower()
            if temp not in seen:  
                seen.add(temp)
        return seen