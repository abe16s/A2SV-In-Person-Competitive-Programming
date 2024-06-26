# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                ones.append(i)
        output = []
        for i in range(len(boxes)):
            current = 0
            for j in ones:
                current += abs(j-i)
            output.append(current)
        return output
        
