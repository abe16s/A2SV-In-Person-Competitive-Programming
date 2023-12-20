class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted = 0
        for c in range(len(strs[0])):
            prev = strs[0][c]
            for r in range(1,len(strs)):
                if strs[r][c] < prev:
                    deleted += 1
                    break
                prev = strs[r][c]
        return deleted