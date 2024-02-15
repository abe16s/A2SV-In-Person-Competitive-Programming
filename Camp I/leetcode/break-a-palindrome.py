class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        flag = False
        for i in range(len(palindrome)):
            if palindrome[i] != "a" and palindrome.count(palindrome[i]) != 1:
                palindrome = palindrome[:i] + "a" + palindrome[i+1:]
                flag = True
                break
        if not flag:
            palindrome = palindrome[:-1] + "b"
        return palindrome