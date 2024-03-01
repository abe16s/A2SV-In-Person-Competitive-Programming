class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        upward_diagonals = set()
        downward_diagonals = set()
        cols = set()
        board = [["."]*n for _ in range(n)]
        cout = []
        def search(level):
            nonlocal upward_diagonals
            nonlocal downward_diagonals
            nonlocal board

            if level >= n:
                copy = [("").join(row) for row in board]
                cout.append(copy)
                return 
            
            for i in range(n):
                if i not in cols and (level + i) not in upward_diagonals and (level - i) not in downward_diagonals:
                    board[level][i] = "Q"
                    upward_diagonals.add(level+i)
                    downward_diagonals.add(level-i)
                    cols.add(i)
                    search(level+1)
                    board[level][i] = "."
                    upward_diagonals.remove(level+i)
                    downward_diagonals.remove(level-i)
                    cols.remove(i)

        search(0)
        return cout