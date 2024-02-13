# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        cur = head
        while cur:
            temp = cur
            cur = cur.next
            temp.next = None
            prev = dummy
            dum = dummy.next
            while dum and dum.val < temp.val:
                prev = prev.next
                dum = dum.next
            prev.next, temp.next = temp, prev.next
        return dummy.next