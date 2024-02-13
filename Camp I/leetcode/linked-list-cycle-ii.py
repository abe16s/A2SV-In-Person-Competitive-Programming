# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = head
        t = head
        cycle = False
        while r and r.next:
            r = r.next.next
            t = t.next
            if r == t:
                cycle = True
                break
        if not cycle:
            return
        r = head
        while r != t:
            r = r.next
            t = t.next
        return t
