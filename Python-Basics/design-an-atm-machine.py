class ATM:

    def __init__(self):
        self.notes = {1:[20,0], 2:[50,0], 3:[100,0], 4:[200,0], 5:[500,0]}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.notes[i+1][1] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        handed_notes = [0, 0, 0, 0, 0]
        i = 5
        while i >= 1 and amount > 0:
            if amount//self.notes[i][0] == 0 and amount >= self.notes[i][0]:
                return [-1]
            current_note = min(amount//self.notes[i][0], self.notes[i][1])
            handed_notes[i-1] = current_note
            amount -= (current_note * self.notes[i][0])
            i -= 1
        if amount:
            return [-1]
        for i in range(5):
            self.notes[i+1][1] -= handed_notes[i]
        return handed_notes 

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)