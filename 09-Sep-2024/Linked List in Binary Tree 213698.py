# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        goal = ""
        cur = head
        while cur:
            goal += str(cur.val)
            cur = cur.next

        def dfs(temp, cur):
            if not cur:
                if len(temp) >= len(goal) and goal in temp:
                    return True
                return False
            if dfs(temp+str(cur.val), cur.right) or dfs(temp+str(cur.val), cur.left):
                return True

        return dfs("", root)
