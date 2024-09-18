# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(1, len(nums)):
            j = i-1
            temp = nums[i]
            while j >= 0 and self.comparator(temp, nums[j]):
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = temp 
        return str(int("".join(map(str, nums))))

    def comparator(self, s1,s2):
        s1 = str(s1)
        s2 = str(s2)
        if s1+s2 > s2+s1:
            return True
        else:
            return False
        