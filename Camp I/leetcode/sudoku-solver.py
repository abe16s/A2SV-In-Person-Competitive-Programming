class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cells = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    cells[(r//3, c//3)].add(board[r][c])

        def search():
            flag = True
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        flag = False
                        break
                if not flag:
                    break

            if flag:
                return True
            
            for i in range(1,10):
                i = str(i)
                if i not in board[r] and i not in cells[(r//3,c//3)] and i not in [board[_][c] for _ in range(9)]:
                    board[r][c] = i
                    cells[(r//3,c//3)].add(i)
                    temp = search()
                    if temp:
                        return True
                    board[r][c] = "."
                    cells[(r//3,c//3)].remove(i)
        search()
