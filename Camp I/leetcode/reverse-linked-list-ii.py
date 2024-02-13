# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right == left:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        while left - 1:
            cur = cur.next
            left -= 1
            right -= 1
        entry = cur
        prev = ListNode(0, cur.next)
        cur = cur.next
        while right:
            cur.next, prev, cur = prev, cur, cur.next
            right -= 1
        entry.next.next, entry.next = cur, prev
        return dummy.next

            
        
        