# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def combiner(ss):
            temp = ""
            for i in range(len(ss)):
                if ss[i] == "1":
                    temp += "0"
                else:
                    temp += "1"
                #temp += str(1 - int(ss[i]))
            return temp
        s = "0"
        for i in range(n-1):
            s = s + "1" + combiner(s)[::-1]
        return s[k-1]
