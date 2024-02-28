class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(visited, r, c, cur, idx):
            if word in cur:
                return True
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                if board[r][c] != word[idx]:
                    return
                visited.add((r,c))
                if (r-1, c) not in visited:
                    up = search(visited, r-1, c, cur+board[r][c], idx+1)
                    if up:
                        return True
                if (r+1, c) not in visited:
                    down = search(visited, r+1, c, cur+board[r][c], idx+1)
                    if down:
                        return True
                if (r, c-1) not in visited:
                    left = search(visited, r, c-1, cur+board[r][c], idx+1)
                    if left:
                        return True
                if (r, c+1) not in visited:
                    right = search(visited, r, c+1, cur+board[r][c], idx+1)
                    if right:
                        return True
                if cur+board[r][c] == word:
                    return True
                visited.remove((r,c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    temp = search(set(), r, c, "", 0)
                    if temp:
                        return True
        return False
                

["a","a","a"],
["A","A","A"],
["a","a","a"]