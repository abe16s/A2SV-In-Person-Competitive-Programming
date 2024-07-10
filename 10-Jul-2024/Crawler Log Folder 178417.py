# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for l in logs:
            if l == "../" and stack:
                stack.pop()
            elif l != "./" and l != "../":
                stack.append(l)
        return len(stack)