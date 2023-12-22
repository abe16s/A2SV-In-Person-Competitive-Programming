class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        up = True
        if arr[1] < arr[0]:
            return False
        for i in range(1,len(arr)-1):
            if arr[i] == arr[i-1] or up == False and arr[i] > arr[i-1]:
                return False
            if arr[i] < arr[i-1]:
                up = False
        if arr[-1] >= arr[-2]:
            return False
        return True