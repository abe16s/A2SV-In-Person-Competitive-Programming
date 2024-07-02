# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if op[0] == "-" or op[-1] == "-":
                x -= 1
            if op[0] == "+" or op[-1] == "+":
                x += 1
        return x