# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        half = math.ceil(len(s)/2)
        chars = sorted(c.keys(), key=lambda x: c[x])
        if c[chars[-1]] > half:
            return ""
        ans = [""]*len(s)
        i = 0
        while c[chars[-1]]:
            ans[i] = chars[-1]
            c[chars[-1]] -= 1
            i += 2
        for ch in range(len(chars)-1):
            while c[chars[ch]]:
                if i >= len(s):
                    i = 1
                ans[i] = chars[ch]
                c[chars[ch]] -= 1
                i += 2
        
        return "".join(ans)