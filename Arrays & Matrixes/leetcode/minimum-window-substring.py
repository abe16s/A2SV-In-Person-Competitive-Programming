class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        cur = defaultdict(int)
        i = 0
        mini = [0,len(s)]
        flag = False
        def check():
            for k in count:
                if cur[k] < count[k]:
                    return False
            return True

        for j in range(len(s)):
            if s[j] in count:
                cur[s[j]] += 1
            while check():
                cur[s[i]] -= 1
                if j-i < mini[1] - mini[0]:
                    mini = [i, j+1]
                    flag = True
                i += 1
        return s[mini[0]:mini[1]] if flag else ""
