# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        i = 0
        for j in range(len(arr2)):
            for k in range(c[arr2[j]]):
                arr1[i] = arr2[j]
                c[arr2[j]] -= 1
                if not arr2[j]:
                    c.pop(arr2[j])
                i += 1
        for k in sorted(c.keys()):
            for v in range(c[k]):
                arr1[i] = k
                i += 1
        return arr1