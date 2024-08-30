# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(cur):
            depth = 0
            l = 0
            r = 0
            if cur.left:
                l = dfs(cur.left)
                if not l:
                    return False
                depth = max(depth, l)
            if cur.right:
                r = dfs(cur.right)
                if not r: 
                    return False
                depth = max(depth, r)
            if abs(r-l) > 1:
                return False
            return depth + 1
        
        return dfs(root)