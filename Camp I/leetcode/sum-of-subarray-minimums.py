class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total = 0
        stack = []
        for i in range(len(arr)):
            x = -1
            while stack and arr[stack[-1][1]] > arr[i]:
                y, j = stack.pop()
                total += arr[j] * (j-y) * (i-j)
            if stack:
                x = stack[-1][1]
            stack.append([x, i])

        while stack:
            y, j = stack.pop()
            total += arr[j] * (j-y) * (len(arr)-j)

        return total % (10**9 + 7)
