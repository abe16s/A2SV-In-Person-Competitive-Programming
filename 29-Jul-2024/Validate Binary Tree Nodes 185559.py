# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                parent[parentX] = parentY

        parent = [i for i in range(n)]
        
        for i in range(n):
            if leftChild[i] != -1:
                if find(leftChild[i]) != leftChild[i] or find(i) == find(leftChild[i]):
                    return False
                union(leftChild[i], i)
            if rightChild[i] != -1:
                if find(rightChild[i]) != rightChild[i] or find(i) == find(rightChild[i]):
                    return False
                union(rightChild[i], i)

        roots = 0
        for i in range(n):
            if parent[i] == i:
                roots += 1
    
        return roots == 1