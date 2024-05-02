# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        carry = 0
        ap = len(a) - 1
        bp = len(b) - 1
        while ap >= 0 or bp >= 0 or carry:
            if ap >= 0:
                carry += int(a[ap])
                ap -= 1
            if bp >= 0:
                carry += int(b[bp]) 
                bp -= 1
            ans.append(str(carry%2))
            carry //= 2
        return ''.join(ans[::-1])