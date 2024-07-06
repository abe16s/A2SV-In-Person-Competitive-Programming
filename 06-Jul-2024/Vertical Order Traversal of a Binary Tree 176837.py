# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        def traverse(cur, row, col):
            if cur:
                cols[col].append([row, cur.val])
                traverse(cur.left, row+1, col-1)
                traverse(cur.right, row+1, col+1)
        traverse(root, 0, 0)
        cout = []
        for k in sorted(cols.keys()):
            cols[k].sort()
            cout.append([cols[k][_][1] for _ in range(len(cols[k]))])
        return cout


