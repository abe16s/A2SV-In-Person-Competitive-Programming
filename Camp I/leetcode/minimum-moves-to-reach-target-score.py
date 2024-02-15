class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ctr = 0
        while target > 1 and maxDoubles:
            if target % 2:
                target -= 1
                ctr += 1
            target = target // 2
            ctr += 1
            maxDoubles -= 1
        return ctr + target - 1