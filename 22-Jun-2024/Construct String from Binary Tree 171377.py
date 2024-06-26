# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(cur):
            if cur is None:
                return ""
            temp = str(cur.val)
            left = preorder(cur.left)
            right = preorder(cur.right)
            if right or left:
                temp += "(" + left + ")"
            if right:
                temp += "(" + right + ")"
            return temp
        
        return preorder(root)