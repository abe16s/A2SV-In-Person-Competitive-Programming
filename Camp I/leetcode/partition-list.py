# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        great = ListNode()
        less_h = less
        great_h = great
        cur = head
        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                great.next = cur
                great = great.next
            cur = cur.next
        less.next = great_h.next
        great.next = None
        return less_h.next