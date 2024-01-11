class Solution:
    def balancedString(self, s: str) -> int:
        goal = len(s) // 4
        count = Counter(s)
        if max(count.values()) <= goal:
            return 0
        i = 0
        j = 0
        mini = float("inf")
        while j < len(s):
            while j < len(s) and max(count.values()) > goal:
                count[s[j]] -= 1
                j += 1
            while max(count.values()) <= goal:
                mini = min(mini,j-i)    
                count[s[i]] += 1
                i += 1
        return mini
            

            