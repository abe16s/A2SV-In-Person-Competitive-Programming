# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = defaultdict(int)
        for i in range(n-1,-1,-1):
            dp[i] = max(dp[i+1+questions[i][1]]+questions[i][0], dp[i+1])
        return max(dp.values())            

            
