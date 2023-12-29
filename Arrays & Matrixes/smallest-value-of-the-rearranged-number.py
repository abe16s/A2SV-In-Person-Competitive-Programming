class Solution:
    def smallestNumber(self, num: int) -> int:        
        if num >= 0:
            num = sorted(str(num))
            i = 0
            zero = 0
            while i < len(num) and num[i] == "0":
                i += 1
            if i < len(num):
                num[i], num[zero] = num[zero], num[i]
            return int("".join(num))
        else:
            num = sorted(str(-num), reverse=True)
            return -int("".join(num))
