class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.ps = []
        for r in range(len(matrix)):
            temp = []
            for c in range(len(matrix[0])):
                cur = matrix[r][c]
                if c-1 >= 0:
                    cur += temp[-1]#self.ps[r][c-1]
                if r-1 >= 0:
                    cur += self.ps[r-1][c]
                if r-1 >= 0 and c-1 >= 0:
                    cur -= self.ps[r-1][c-1]
                temp.append(cur)
            self.ps.append(temp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        cout = self.ps[row2][col2]
        if col1-1 >= 0:
            cout -= self.ps[row2][col1-1]
        if row1-1 >= 0:
            cout -= self.ps[row1-1][col2]
        if row1-1 >= 0 and col1-1 >= 0:
            cout += + self.ps[row1-1][col1-1]
        return cout


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)