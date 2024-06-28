# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0 
        k = 0
        while i<len(chars):
            cur = chars[i]
            ctr = 0
            while i < len(chars) and cur == chars[i]:
                ctr += 1
                i += 1
            chars[k] = cur
            k += 1
            if ctr > 1:
                for j in str(ctr):
                    chars[k] = j
                    k += 1
        return k