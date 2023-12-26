class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        i = 0
        while i < len(mat):
            total += mat[i][i] 
            i+=1
        
        j = [0,len(mat)-1]
        while j[0] < len(mat):
            total += mat[j[0]][j[1]]
            j[0]+=1
            j[1]-=1
        
        if len(mat) % 2:
            total -= mat[len(mat)//2][len(mat)//2]
        
        return total