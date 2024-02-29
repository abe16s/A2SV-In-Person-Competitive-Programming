# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        maxi = [-1,-1]
        for i in range(len(nums)):
            maxi = max(maxi, [nums[i], i])

        root = TreeNode(maxi[0])
        root.left = self.constructMaximumBinaryTree(nums[:maxi[1]])
        root.right = self.constructMaximumBinaryTree(nums[maxi[1]+1:])

        return root