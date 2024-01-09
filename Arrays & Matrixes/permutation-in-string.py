class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = collections.Counter(s1)
        k = len(s1)
        cur = collections.Counter(s2[:k])
        if cur == c:
            return True
        i = k
        while i < len(s2):
            cur[s2[i-k]] -= 1
            if cur[s2[i-k]] <= 0:
                cur.pop(s2[i-k])
            cur[s2[i]] += 1
            if cur == c:
                return True
            i += 1
        return False