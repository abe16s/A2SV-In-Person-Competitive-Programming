class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        for row in matrix:
            for i in range(1,len(matrix[0])):
                row[i] += row[i-1]
        
        ctr = 0
        for i in range(len(matrix[0])):
            for j in range(i, len(matrix[0])):
                dic = defaultdict(int)
                dic[0] += 1
                rs = 0
                for r in range(len(matrix)):
                    rs += matrix[r][j] - (matrix[r][i-1] if i-1>=0 else 0)
                    ctr += dic[rs-target]
                    dic[rs] += 1

        return ctr