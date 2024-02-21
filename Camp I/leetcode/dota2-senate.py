class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)
        n = len(senate)
        while r and d:
            if r[0] < d[0]:
                r.append(n)
            else:
                d.append(n)
            r.popleft()
            d.popleft()
            n += 1
        if r:
            return "Radiant"
        return "Dire"