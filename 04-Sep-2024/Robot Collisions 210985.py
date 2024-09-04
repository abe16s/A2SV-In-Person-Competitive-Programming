# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        z = sorted([[positions[i], i] for i in range(n)])
        stack = []
        surviving = []
        for i in range(n):
            if directions[z[i][-1]] == 'R':
                stack.append(z[i][-1])
            else:
                while stack and healths[stack[-1]] < healths[z[i][-1]]:
                    stack.pop()
                    healths[z[i][-1]] -= 1
                if stack and healths[stack[-1]] == healths[z[i][-1]]:
                    stack.pop()
                elif stack and healths[stack[-1]] > healths[z[i][-1]]:
                    healths[stack[-1]] -= 1
                elif not stack:
                    surviving.append(z[i][-1])
        surviving.extend(stack)
        surviving.sort()

        for s in range(len(surviving)):
            surviving[s] = healths[surviving[s]]

        return surviving


