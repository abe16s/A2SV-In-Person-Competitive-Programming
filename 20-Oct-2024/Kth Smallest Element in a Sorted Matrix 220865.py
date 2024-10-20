# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in matrix:
            heap+=i
        heapq.heapify(heap)
        for i in range(k):
            cout = heapq.heappop(heap)
        
        return cout