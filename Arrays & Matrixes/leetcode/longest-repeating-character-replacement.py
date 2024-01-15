class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        maxi = 0
        j = 0
        for i in range(len(s)):
            window[s[i]] += 1
            if sum(window.values()) -  max(window.values()) <= k:
                maxi = max(maxi, i-j+1)
            while sum(window.values()) -  max(window.values()) > k:
                window[s[j]] -= 1
                j += 1
        return maxi