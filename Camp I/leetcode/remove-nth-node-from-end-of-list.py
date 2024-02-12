# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cout = ListNode()
        cout.next = head
        f = cout
        s = cout
        while f:
            if n < 0:
                s = s.next
            f = f.next
            n -= 1
        s.next = s.next.next
        return cout.next