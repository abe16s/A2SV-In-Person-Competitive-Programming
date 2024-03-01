class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        upward_diagonals = set()
        downward_diagonals = set()
        cols = set()
        cout = 0
        def search(level):
            nonlocal upward_diagonals
            nonlocal downward_diagonals
            nonlocal cout

            if level >= n:
                nonlocal cout
                cout += 1
                return 
            
            for i in range(n):
                if i not in cols and (level + i) not in upward_diagonals and (level - i) not in downward_diagonals:
                    upward_diagonals.add(level+i)
                    downward_diagonals.add(level-i)
                    cols.add(i)
                    search(level+1)
                    upward_diagonals.remove(level+i)
                    downward_diagonals.remove(level-i)
                    cols.remove(i)

        search(0)
        return cout