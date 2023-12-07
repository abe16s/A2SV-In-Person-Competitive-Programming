class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()
        for ran in ranges:
            for i in range(ran[0], ran[1]+1):
                covered.add(i)
        for j in range(left, right+1):
            if j not in covered:
                return False
        return True