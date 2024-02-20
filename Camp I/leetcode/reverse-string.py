class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(x,y):
            if x < y:
                s[x], s[y] = s[y], s[x]
                reverse(x+1, y-1)
        
        reverse(0,len(s)-1)