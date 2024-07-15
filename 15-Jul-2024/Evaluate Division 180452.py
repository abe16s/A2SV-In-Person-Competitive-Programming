# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        related = defaultdict(set)
        variables = set()
        for i in range(len(equations)):
            related[equations[i][0]].add(( values[i], equations[i][1]))
            related[equations[i][1]].add((1/values[i], equations[i][0])) 
            variables.add(equations[i][0])
            variables.add(equations[i][1])

        def dfs(start, end, visited):
            if start[0] == end:
                return start[1]
            if start[0] not in visited:
                visited.add(start[0])
                cur = -1
                for times, var in related[start[0]]:
                    val = dfs([var, times*start[1]], end, visited)
                    if val != -1:
                        cur = val
                        break
                return cur
            return -1

        cout = []
        for q in range(len(queries)):
            if queries[q][0] in variables and queries[q][1] in variables:
                val = dfs([queries[q][0], 1], queries[q][1], set())
                cout.append(val)
            else:
                cout.append(-1)
        return cout
