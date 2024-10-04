# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        if len(citations)==1:
            return 1 if citations[0] else 0
        elif citations[-1]>=len(citations):
            return len(citations)
        for i in range(len(citations)):
            if citations[i]<i+1:
                break
        return i