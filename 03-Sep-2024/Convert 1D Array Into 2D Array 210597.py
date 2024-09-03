# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        matrix = []
        c = 0
        for r in range(m):
            matrix.append(original[c:c+n])
            c += n
        return matrix
