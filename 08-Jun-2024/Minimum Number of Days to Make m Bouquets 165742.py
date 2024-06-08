# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def bouquets(day):
            b = 0
            conseq = 0
            for bloom in bloomDay:
                if bloom <= day:
                    conseq += 1
                else:
                    b += conseq // k
                    conseq = 0 
            b += conseq // k
            return b
        maxi = max(bloomDay)
        l = 0
        r = maxi
        while l <= r:
            mid = l + (r-l)//2
            if bouquets(mid) >= m:
                r = mid - 1
            else:
                l = mid + 1
        return l if l <= maxi else -1

        
