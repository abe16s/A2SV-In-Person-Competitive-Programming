# Problem: Balance a binary search tree - https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(cur):
            if not cur:
                return
            inorder(cur.left)
            nums.append(cur.val)
            inorder(cur.right)
        inorder(root)

        def balance(start, end):
            if start >= end:
                return None
            middle = start + (end-start) // 2
            root = TreeNode(nums[middle])
            root.left = balance(start, middle)
            root.right = balance(middle+1, end)
            return root
        
        return balance(0, len(nums))



