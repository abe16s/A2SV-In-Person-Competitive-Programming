# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		color = [0] * V
		def dfs(prev, node):
		    for nbr in adj[node]:
		        if nbr != prev:
		            if (color[nbr] == 1):
		                return True 
		            if color[nbr] == 0:
		                color[nbr] = 1
		                if dfs(node, nbr):
		                    return True
		    color[node] = 2
		    return False
		for i in range(V):
		    if color[i] == 0:
		        color[i] = 1
		        if dfs(-1, i):
		            return True
		return False