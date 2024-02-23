# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cout = 0
        def inorder(node):
            if node:
                nonlocal k
                inorder(node.left)
                if k == 1:
                    nonlocal cout
                    cout = node.val
                    k -= 1
                    return 
                k -= 1
                if k < 1:
                    return
                inorder(node.right)

        inorder(root)
        
        return cout