class Solution:
    def totalMoney(self, n: int) -> int:
        week = n//7
        total = 0 
        for i in range(week):
            total += (28+(7*i))
        for i in range(n%7):
            total += (i+week+1)
        return total            
