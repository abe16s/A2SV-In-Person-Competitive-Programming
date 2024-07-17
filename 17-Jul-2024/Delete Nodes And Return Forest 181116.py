# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        cout = []
        to_del = set(to_delete)
        def dfs(node, parent):
            if not node:
                return
            par = node if node.val not in to_del else None 
            dfs(node.left, par)
            dfs(node.right, par)
            if node.left and node.left.val in to_del:
                node.left = None
            if node.right and node.right.val in to_del:
                node.right = None
            if parent is None and node.val not in to_del:
                cout.append(node)
    
        dfs(root, None)
        return cout