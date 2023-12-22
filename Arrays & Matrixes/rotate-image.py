class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        turns = ceil(len(matrix)/2)
        row = len(matrix) - 1
        col = len(matrix[0]) - 1
        for turn in range(turns):
            rowTop = matrix[turn][turn:row-turn+1]
            rowBottom = matrix[row-turn][turn:row-turn+1]
            colLeft = [matrix[curRow][turn] for curRow in range(row-turn-1, turn, -1)]
            colRight = [matrix[curRow][row-turn] for curRow in range(row-turn-1, turn, -1)]
            for r in range(turn, row-turn+1):
                matrix[r][row-turn] = rowTop[r-turn]
            for r in range(turn, row-turn+1):
                matrix[r][turn] = rowBottom[r-turn]
            for c in range(turn+1, row-turn):
                matrix[turn][c] = colLeft[c-turn-1]
            for c in range(turn+1, row-turn):
                matrix[row-turn][c] = colRight[c-turn-1]
    
