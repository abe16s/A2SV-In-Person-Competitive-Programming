class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        ctr = 1
        prev = arr[0]
        for i in range(1, len(arr)):
            if arr[i] == prev:
                ctr += 1
            else:
                ctr = 1
                prev = arr[i]
            if ctr*4 > len(arr):
                return arr[i]