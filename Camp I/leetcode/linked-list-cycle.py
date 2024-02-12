# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        r = head
        t = head
        while r and r.next:
            r = r.next.next
            t = t.next
            if t == r:
                return True
        return False