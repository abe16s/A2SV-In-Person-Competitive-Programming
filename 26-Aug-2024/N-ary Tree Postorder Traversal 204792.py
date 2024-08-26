# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        cout = []
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp:
                cout.append(temp.val)
                for c in temp.children:
                    stack.append(c)

        return cout[::-1]