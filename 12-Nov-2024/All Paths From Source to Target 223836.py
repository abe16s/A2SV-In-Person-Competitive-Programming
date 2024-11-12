# Problem: All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        return self.backtrack(0, [0])
    
    def backtrack(self, node, cur_path):
        if node == len(self.graph)-1:
            return [cur_path[:]]
        paths = []
        for nbr in self.graph[node]:
            cur_path.append(nbr)
            paths.extend(self.backtrack(nbr, cur_path))
            cur_path.pop()
        return paths
