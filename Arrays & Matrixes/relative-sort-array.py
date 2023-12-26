class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        min_idx = 0
        for i in range(len(arr2)):
            for j in range(min_idx, len(arr1)):
                if arr2[i] == arr1[j]:
                    arr1[min_idx], arr1[j] = arr1[j], arr1[min_idx]
                    min_idx += 1
        arr1[min_idx:] = sorted(arr1[min_idx:])
        return arr1