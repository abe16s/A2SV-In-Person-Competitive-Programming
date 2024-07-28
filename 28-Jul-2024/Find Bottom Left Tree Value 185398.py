# Problem: Find Bottom Left Tree Value - https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        leftmosts = []
        while queue:
            leftmost = None
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    if not leftmost:
                        leftmost = cur
                        leftmosts.append(leftmost)
                    queue.append(cur.left)
                    queue.append(cur.right)

        return leftmosts[-1].val