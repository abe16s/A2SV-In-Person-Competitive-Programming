class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cout = []
        cur = set()
        c = Counter(s)
        l = 0
        while l < len(s):
            r = l
            while r < len(s):
                cur.add(s[r])
                c[s[r]] -= 1
                if c[s[r]] == 0:
                    cur.remove(s[r])
                r += 1
                if not cur:
                    break
            cout.append(r-l)
            l = r
        return cout