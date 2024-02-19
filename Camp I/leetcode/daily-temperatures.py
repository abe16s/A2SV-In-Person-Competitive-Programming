class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        cout = [0] * len(temperatures)
        for t in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[t]:
                temp = stack.pop()
                cout[temp[-1]] = t-temp[-1]
            stack.append([temperatures[t], t])
        return cout
