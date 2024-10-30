# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def traverse(node, num):
            if not node.left and not node.right:
                nonlocal total
                total += int(num + str(node.val))
                return 
            if node.left:
                traverse(node.left, num + str(node.val))
            if node.right:
                traverse(node.right, num + str(node.val))
        traverse(root, "")
        return total
