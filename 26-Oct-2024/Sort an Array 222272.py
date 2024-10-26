# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(cur):
            if len(cur) <= 1:
                return cur
            mid = len(cur)//2
            left = merge(cur[:mid])
            right = merge(cur[mid:])
            merged = []
            l = 0
            r = 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
            
            while l < len(left):
                merged.append(left[l])
                l += 1 

            while r < len(right):
                merged.append(right[r])
                r += 1

            return merged


        return merge(nums)