# Problem: Different Ways to Add Parentheses - https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def dfs(expression):
            if expression in m:
                return m[expression]
            if expression.isdigit():
                m[expression] = [int(expression)]
                return [int(expression)]
            ret = []
            for i, c in enumerate(expression):
                if c in "+-*":
                    l = dfs(expression[:i])
                    r = dfs(expression[i+1:])
                    ret.extend(eval(str(x)+c+str(y)) for x in l for y in r)
            m[expression] = ret
            return ret
        
        m = {}
        return dfs(expression)
        