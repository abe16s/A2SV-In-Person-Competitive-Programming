# Problem: Design an Ordered Stream - https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.n = n        
        self.nextInLine = 1
        self.store = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        output = []
        if idKey == self.nextInLine:
            output.append(value)
            i = idKey + 1
            while i in self.store:
                output.append(self.store[i])
                i += 1
            self.nextInLine = i
        else:
            self.store[idKey] = value
        return output



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)