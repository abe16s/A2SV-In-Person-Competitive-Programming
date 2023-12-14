class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.ones = 0
        self.flipp = 0
        self.bits = [0 for i in range(size)]

    def fix(self, idx: int) -> None:
        if self.flipp % 2 == 0 and self.bits[idx] != 1:
            self.bits[idx] = 1
            self.ones += 1
        elif self.flipp % 2 == 1 and self.bits[idx] != 0:
            self.bits[idx] = 0
            self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.flipp % 2 == 0 and self.bits[idx] != 0:
            self.bits[idx] = 0
            self.ones -= 1
        elif self.flipp % 2 == 1 and self.bits[idx] != 1:
            self.bits[idx] = 1
            self.ones -= 1

    def flip(self) -> None:
        self.flipp += 1
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size
        if self.flipp % 2 == 0:
            return self.ones == self.size
        else:
            return self.size - self.ones == self.size

    def one(self) -> bool:
        return self.ones >= 1    
        if self.flipp % 2 == 0:
            return self.ones >= 1
        else:
            return self.size - self.ones >= 1

    def count(self) -> int:
        return self.ones
        if self.flipp % 2 == 0:
            return self.ones
        else:
            return self.size - self.ones

    def toString(self) -> str:
        if self.flipp % 2 == 1:
            for i in range(self.size):
                self.bits[i] = 1 - self.bits[i]
                self.flipp = 0
        return "".join(map(str, self.bits))

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()