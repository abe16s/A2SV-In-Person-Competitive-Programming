from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        if k > len(p):
            return []
        cout = []
        wanted = Counter(p)
        start = 0
        window = Counter(s[:k])
        while start <= len(s) - k:
            if wanted == Counter(s[start:start+k]):
                cout.append(start)
            start+=1


        return cout