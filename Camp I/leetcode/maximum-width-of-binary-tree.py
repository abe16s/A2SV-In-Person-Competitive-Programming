# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        rows = defaultdict(lambda: [float("inf"), -float("inf")])
        width = 0
        def dfs(cur, row, col):
            if cur:
                temp = rows[row]
                rows[row] = [min(temp[0], col), max(temp[1],col)]
                dfs(cur.left, row+1, 2*col)
                dfs(cur.right, row+1, 2*col+1)
        dfs(root, 0,0)
        for r in rows:
            width = max(width, rows[r][1]-rows[r][0]+1)
        return width
            