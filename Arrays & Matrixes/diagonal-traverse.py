class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up = True
        r = 0
        c = 0
        output = []
        while r < len(mat) and c < len(mat[0]):
            output.append(mat[r][c])
            if up:
                if r-1 >= 0 and c+1 < len(mat[0]):
                    r -= 1
                    c += 1
                elif c+1 < len(mat[0]):
                    c += 1
                    up = False
                elif r+1 < len(mat):
                    r += 1
                    up = False
                else:
                    break
            else:
                if r+1 < len(mat) and c-1 >= 0:
                    r += 1
                    c -= 1
                elif r+1 < len(mat):
                    r += 1
                    up = True
                elif c+1 < len(mat[0]):
                    c += 1
                    up = True    
                else:
                    break
        return output
