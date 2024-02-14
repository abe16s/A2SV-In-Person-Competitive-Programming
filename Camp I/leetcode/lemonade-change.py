class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for b in bills:
            if b == 5:
                five += 5
            elif b == 10:
                ten += 10
                five -= 5
            else:
                if ten:
                    ten -= 10
                    five -= 5
                else:
                    five -= 15
            if five < 0:
                return False
        return True