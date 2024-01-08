class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0
        l = r = 0
        cur = set()
        ctr = 0
        while r < len(s):
            if s[r] not in cur:
                cur.add(s[r])
                ctr += 1
                r += 1
                _max = max(_max, ctr)
            else:
                while l < r and s[l] != s[r]:
                    cur.remove(s[l])
                    l += 1
                    ctr -= 1
                cur.remove(s[l])
                ctr -= 1
                l += 1

        return _max

