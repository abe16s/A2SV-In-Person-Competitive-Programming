# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ctr = 0
        def recur(node):
            if not node:
                return (0,0)
            nonlocal ctr
            a1, b1 = recur(node.left)
            a2, b2 = recur(node.right)
            total = (a1 + a2 + node.val)
            qty = (b1 + b2 + 1)
            if total // qty == node.val:
                ctr += 1
            return (total, qty)
        recur(root)
        return ctr