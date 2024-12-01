# Problem: Construct Binary Tree from Preorder and Inorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder_index_map = {}
        self.peorder_idx = 0
        for index, value in enumerate(inorder):
            self.inorder_index_map[value] = index

        return self.helper(0, len(preorder)-1)
        
    def helper(self, left, right):
        if left > right :
            return None

        root_value = self.preorder[self.peorder_idx]
        node = TreeNode(root_value)
        self.peorder_idx += 1
        node.left = self.helper(left, self.inorder_index_map[root_value] - 1)
        node.right = self.helper(self.inorder_index_map[root_value] + 1, right)
        return node