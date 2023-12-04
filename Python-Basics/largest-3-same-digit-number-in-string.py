class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cur = 1
        prev = num[0]
        maxi = 0
        cout = ""
        for i in range(1, len(num)):
            if num[i] == prev:
                cur += 1
            else:
                cur = 1
                prev = num[i]
            if cur == 3:
                if maxi <= int(num[i-2:i+1]):
                    maxi = int(num[i-2:i+1])
                    cout = num[i-2:i+1]
        return cout