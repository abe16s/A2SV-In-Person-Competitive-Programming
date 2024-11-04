# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        cout=[]
        for i in range(len(l)):
            x=nums[l[i]:r[i]+1]
            x.sort()
            flag="true"  
            for i in range(len(x)-1):
                if (x[1]-x[0])!=(x[i+1]-x[i]):
                    flag=""
            cout.append(flag)
        return cout