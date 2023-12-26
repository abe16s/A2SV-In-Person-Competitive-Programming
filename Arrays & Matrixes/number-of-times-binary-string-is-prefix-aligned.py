class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ctr = 0
        maxi = 0
        for i in range(len(flips)):
            maxi = max(maxi, flips[i])
            if i+1 == maxi:
                ctr += 1
        return ctr
            
