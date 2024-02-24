# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def recurse(cur):
            if cur:
                a = recurse(cur.left)
                b = recurse(cur.right)
                s = a[0]+b[0]+cur.val
                if a[3] == float("inf"):
                    a[3] = cur.val-1
                if b[2] == -float("inf"):
                    b[2] = cur.val+1
                bst = a[1] and b[1] and (a[2] < cur.val < b[3]) and (a[3] < cur.val < b[2])
                if bst:
                    nonlocal max_sum
                    max_sum = max(max_sum, s)
                mi = cur.val
                if a[2] != -float("inf"):
                    mi = min(mi, a[2])
                if b[2] != -float("inf"):
                    mi = min(mi, b[2])

                ma = cur.val
                if a[3] != float("inf"):
                    ma = max(ma, a[3])
                if b[3] != float("inf"):
                    ma = max(ma, b[3])  


                return [s, bst, mi, ma] #sum, isBST, min, max
            return [0, True, -float("inf"), float("inf")]

        recurse(root)
        return max_sum