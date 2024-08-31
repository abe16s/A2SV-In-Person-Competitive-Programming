# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for o in operations:
            if o.isdigit() or (o.startswith('-') and o[1:].isdigit()):
                record.append(int(o))
            elif o == "+":
                a = record[-1]
                b = record[-2]
                record.append(a+b)
            elif o == "D":
                record.append(record[-1]*2)
            elif o == "C":
                record.pop()
        return sum(record)
