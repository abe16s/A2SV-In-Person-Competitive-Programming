class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float("inf")

    def push(self, val: int) -> None:
        self.mini = min(self.mini, val)
        self.stack.append([val, self.mini])

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.mini = self.stack[-1][1]
        else:
            self.mini = float("inf")

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()