# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        out=[]
        if len(changed)%2:
            return out     
        changed.sort() 
        count=Counter(changed)
        i=0
        while i< len(changed):
            x=changed[i]   
            if x==0 and count[x]>=2:
                count[x]-=2
                out.append(x)
            elif x>0 and count[x] and count[x*2]:
                out.append(x)
                count[x]-=1
                count[x*2]-=1
            i+=1
        return out if len(out) == len(changed)//2 else []