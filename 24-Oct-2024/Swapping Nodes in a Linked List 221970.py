# Problem: Swapping Nodes in a Linked List - https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            if n == k:
                begin = cur
            cur = cur.next

        k = n-k+1
        cur = head
        n = 0
        while cur:
            n += 1
            if n == k:
                end = cur
            cur = cur.next
        
        begin.val, end.val = end.val, begin.val
        return head