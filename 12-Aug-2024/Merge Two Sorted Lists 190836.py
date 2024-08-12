# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            cur = list1
            temp = cur.next
            cur.next = None
            list1 = temp
        else:
            cur = list2
            temp = cur.next
            cur.next = None
            list2 = temp
        
        cur.next = self.mergeTwoLists(list1, list2)
        return cur