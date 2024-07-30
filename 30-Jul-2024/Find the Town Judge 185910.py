# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = -1
        trustee = [0] * n
        trusts = [False for _ in range(n)]

        for a, b in trust:
            trusts[a-1] = True
            trustee[b-1] += 1
        
        for i in range(n):
            if trustee[i] == n-1 and trusts[i] == False:
                judge = i + 1
                break

        return judge 
