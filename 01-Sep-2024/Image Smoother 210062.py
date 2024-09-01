# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def getCell(row, col):
            if 0 <= row < len(img) and 0<= col < len(img[0]):
                return img[row][col]
            return -1
        output = []
        for row in range(len(img)):
            cur = []
            for col in range(len(img[0])):
                total = img[row][col]
                ctr = 1
                if getCell(row-1, col-1) >= 0:
                    total += getCell(row-1, col-1)
                    ctr += 1
                if getCell(row-1, col) >= 0:
                    total += getCell(row-1, col)
                    ctr += 1
                if getCell(row-1, col+1) >= 0:
                    total += getCell(row-1, col+1)
                    ctr += 1
                if getCell(row, col-1) >= 0:
                    total += getCell(row, col-1)
                    ctr += 1
                if getCell(row, col+1) >= 0:
                    total += getCell(row, col+1)
                    ctr += 1
                if getCell(row+1, col-1) >= 0:
                    total += getCell(row+1, col-1)
                    ctr += 1
                if getCell(row+1, col) >= 0:
                    total += getCell(row+1, col)
                    ctr += 1
                if getCell(row+1, col+1) >= 0:
                    total += getCell(row+1, col+1)
                    ctr += 1
                cur.append(total//ctr)
            output.append(cur)
        return output
                
                    
