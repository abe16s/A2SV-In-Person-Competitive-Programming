import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passAt = [0] * 1001
        for t in trips:
            curPass, start, end = t
            passAt[start] += curPass
            passAt[end] -= curPass

        cur = 0
        for i in passAt:
            cur += i
            if cur > capacity:
                return False
        return True