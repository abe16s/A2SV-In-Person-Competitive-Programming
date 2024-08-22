# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
             board[click[0]][click[1]] = "X"
             return board

        neighbours = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        def dfs(r, c):
            mines = 0
            for nbr_r, nbr_c in neighbours:
                nbr_r += r
                nbr_c += c
                if 0 <= nbr_r < len(board) and 0 <= nbr_c < len(board[0]):
                    if board[nbr_r][nbr_c] == "M":
                        mines += 1
                    
            if mines == 0:
                board[r][c] = "B"
                for nbr_r, nbr_c in neighbours:
                    nbr_r += r
                    nbr_c += c
                    if 0 <= nbr_r < len(board) and 0 <= nbr_c < len(board[0]):
                        if board[nbr_r][nbr_c] == "E":
                            dfs(nbr_r, nbr_c)
            else:
                board[r][c] = str(mines)

        dfs(click[0], click[1])
        return board
