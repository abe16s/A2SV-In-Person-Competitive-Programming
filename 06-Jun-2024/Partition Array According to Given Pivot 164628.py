# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        equal = []
        for num in nums:
            if num == pivot:
                equal.append(num)
            elif num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
        return less + equal + greater