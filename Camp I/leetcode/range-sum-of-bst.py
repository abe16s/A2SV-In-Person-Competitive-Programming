# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        def dfs(cur):
            nonlocal total
            if cur:
                if low <= cur.val <= high:
                    total += cur.val
                dfs(cur.left)
                dfs(cur.right)
        dfs(root)

        return total