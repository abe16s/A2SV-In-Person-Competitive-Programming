class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cells = [["." for _ in range(n)] for _ in range(m)]
        for wx, wy in walls:
            cells[wx][wy] = "W"
        #horizontal
        for g in guards:
            gy, gx = g[0], g[1]+1
            while gx < n and cells[gy][gx] == ".":
                cells[gy][gx] = "H"
                gx += 1
            gx = g[1]
            while gx >= 0 and cells[gy][gx] == ".":
                cells[gy][gx] = "H"
                gx -= 1
        #vertical 
        for g in guards:
            gy, gx = g[0]+1, g[1]
            while gy < m and cells[gy][gx] in ".H":
                cells[gy][gx] = "V"
                gy += 1
            gy = g[0]
            while gy >= 0 and cells[gy][gx] in ".H":
                cells[gy][gx] = "V"
                gy -= 1
        
        output = 0
        for r in range(m):
            for c in range(n):
                if cells[r][c] ==".":
                    output += 1
        return output