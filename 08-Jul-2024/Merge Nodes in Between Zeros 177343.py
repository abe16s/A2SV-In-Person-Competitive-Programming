# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head.next
        temp = head
        between = 0
        while True:
            if node.val:
                between += node.val
            else:
                temp.val = between
                if not node.next:
                    temp.next = None
                    return head
                temp = temp.next
                between = 0
            node = node.next
