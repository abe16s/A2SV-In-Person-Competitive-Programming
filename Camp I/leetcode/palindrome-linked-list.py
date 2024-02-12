# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = ListNode()
        cur = head
        while cur:
            temp = ListNode(cur.val)
            temp.next = reverse
            reverse = temp
            cur = cur.next
        
        cur = head
        while cur:
            if cur.val != reverse.val:
                return False
            cur = cur.next
            reverse = reverse.next
            
        return True

        

        