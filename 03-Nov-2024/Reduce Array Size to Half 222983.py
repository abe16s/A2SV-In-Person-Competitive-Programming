# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c=Counter(arr)
        l=len(arr)//2
        size=ctr=0
        y=[i for i in c.values()]
        y.sort(reverse=True)
        for j in y:
            ctr+=j
            size+=1 
            if ctr>=l:
                break           
        return size
