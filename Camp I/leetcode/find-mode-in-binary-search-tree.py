# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        def traverse(cur):
            if cur:
                freq[cur.val] = freq.get(cur.val, 0) + 1
                traverse(cur.left)
                traverse(cur.right)
        traverse(root)
        maxi = max(freq.values())
        cout = []
        for k in freq:
            if freq[k] == maxi:
                cout.append(k)
        return cout

