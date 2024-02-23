# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cout = []
        def inorder(cur):
            if cur:
                inorder(cur.left)
                cout.append(cur.val)
                inorder(cur.right)
        inorder(root)

        for i in range(len(cout)-1):
            if cout[i] >= cout[i+1]:
                return False
        return True