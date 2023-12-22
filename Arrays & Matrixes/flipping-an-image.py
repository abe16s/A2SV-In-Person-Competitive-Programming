class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            l = 0
            r = len(row) - 1
            while l < r:
                row[l], row[r] = 1 - row[r], 1 - row[l]
                l += 1
                r -= 1
            if len(row) % 2:
                row[len(row)//2] = 1 - row[len(row)//2]
        return image