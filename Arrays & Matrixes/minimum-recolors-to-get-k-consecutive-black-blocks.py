class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        mini = float("inf")
        j = 0
        i = 0
        for j in range(len(blocks)):
            if j >= k:
                mini = min(mini, white)
                if blocks[i] == "W":
                    white -= 1
                i += 1
            if blocks[j] == "W":
                white += 1
        if j+1 >= k:
            mini = min(mini, white)

        return mini if mini != float("inf") else 0 