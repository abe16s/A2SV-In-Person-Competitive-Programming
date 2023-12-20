class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposee = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                transposee[c][r] = matrix[r][c]
        return transposee