# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        if k >= length:
            part = 1
            remainder = 0
        else:
            part = length // k
            remainder = length % k
        
        cur = head
        i = 0
        cout = []
        while cur:
            cout.append(cur)
            for i in range(part-1):
                cur = cur.next
            if remainder > 0:
                cur = cur.next
            cur.next, cur  = None, cur.next
            remainder -= 1
        
        for l in range(k-len(cout)):
            cout.append(None)
        return cout

