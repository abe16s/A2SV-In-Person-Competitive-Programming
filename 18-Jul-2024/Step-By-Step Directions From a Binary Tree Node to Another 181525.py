# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node, goal):
            if not node:
                return False
            if node.val == goal:
                return [""]
            l = dfs(node.left, goal)
            if l:
                return ["L" + l[0]]
            r = dfs(node.right, goal)
            if r:
                return ["R" + r[0]]        
        
        s = dfs(root, startValue)[0]
        d = dfs(root,destValue)[0]
        i = 0
        while i < min(len(s), len(d)):
            if s[i] == d[i]:
                i += 1
            else:
                break
        s = s[i:]
        d = d[i:]

        return len(s)*"U" + d