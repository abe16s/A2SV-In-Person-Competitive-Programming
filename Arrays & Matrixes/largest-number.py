class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n=[str(i) for i in nums]
        cout=""
        while len(n)>0:
            i=0
            while i<len(n):
                x=n[i]
                for y in n:
                    if x+y<y+x:
                        x=y
                n.remove(x)
                cout+=x
        return str(int(cout))

        
            

        
