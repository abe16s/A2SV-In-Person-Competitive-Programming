# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def search(cur):
            if not cur.left and not cur.right:
                return [cur.val, cur.val]
            a = [float("inf"),-1]
            if cur.left:
                temp = search(cur.left)
                a = [min(a[0], temp[0]), max(a[1], temp[1])]
            if cur.right:
                temp = search(cur.right)
                a = [min(a[0], temp[0]), max(a[1], temp[1])]
            nonlocal maxi
            maxi = max(maxi, abs(a[0] - cur.val), abs(a[1]-cur.val))
            return [min(a[0], cur.val), max(a[1], cur.val)]

        search(root)

        return maxi                