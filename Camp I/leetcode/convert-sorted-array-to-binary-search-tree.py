# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def BST(start, end):
            if end <= start:
                return None
            if end-start == 1:
                return TreeNode(nums[start])
            middle = start + (end-start)//2 
            root = TreeNode(nums[middle])
            l = BST(start, middle)
            r = BST(middle+1, end)
            root.left = l
            root.right = r
            return root
        
        return BST(0, len(nums))