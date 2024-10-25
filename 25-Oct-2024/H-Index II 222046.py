# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations) - 1
        while l <= r:
            mid = (l + r) // 2
            if len(citations) - mid == citations[mid]:
                return len(citations) - mid
            elif len(citations) - mid < citations[mid]:
                r = mid - 1        
            else:
                l = mid + 1 

        return len(citations) - l