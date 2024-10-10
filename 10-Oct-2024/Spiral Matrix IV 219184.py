# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1]*n for _ in range(m)]
        cur = head
        sr = sc = 0
        er, ec = m-1, n-1 
        while cur:
            for i in range(sc,ec+1):
                if not cur:
                    return matrix
                matrix[sr][i] = cur.val
                cur = cur.next

            for i in range(sr+1, er+1):
                if not cur:
                    return matrix
                matrix[i][ec] = cur.val
                cur = cur.next

            for i in range(ec-1,sc-1,-1):
                if not cur:
                    return matrix
                matrix[er][i] = cur.val
                cur = cur.next

            for i in range(er-1, sr, -1):
                if not cur:
                    return matrix
                matrix[i][sc] = cur.val
                cur = cur.next 
            sr += 1
            sc += 1
            er -= 1
            ec -= 1
            
        return matrix
