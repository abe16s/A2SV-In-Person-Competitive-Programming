# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds =  ListNode()
        evens = ListNode()
        odds_org = odds
        evens_org = evens
        i = 1
        cur = head
        while cur:
            if i % 2:
                odds.next = cur
                odds = odds.next
            else:
                evens.next = cur
                evens = evens.next
            cur = cur.next
            i += 1
        odds.next = evens_org.next
        evens.next = None
        return odds_org.next