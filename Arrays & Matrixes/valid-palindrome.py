class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for i in s:
            if i.isalnum():
                ss += i.lower()
        i = 0
        j = len(ss)-1
        while j >= i:
            if ss[i] != ss[j]:
                return False
            i += 1
            j -= 1
        return True 