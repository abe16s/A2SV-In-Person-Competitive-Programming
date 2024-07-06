# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        cur = []
        def search(idx):
            if idx >= len(num):
                return len(cur) >= 3
            
            for i in range(idx, len(num)):
                val = num[idx:i+1]
                if val[0] == "0" and len(val) > 1:
                    continue
                if len(cur) > 1 and int(val) != cur[-1] + cur[-2]:
                    continue
                cur.append(int(val))
                temp = search(i+1)
                if temp:
                    return True
                cur.pop()
        return search(0)
