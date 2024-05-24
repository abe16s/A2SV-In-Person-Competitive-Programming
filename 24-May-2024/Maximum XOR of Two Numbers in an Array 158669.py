# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def addNum(self, num, root):
        current = root
        for ch in num:
            if ch not in current:
                current[ch] = {}
            current = current[ch]

    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}
        bits = {}
        for num in nums:
            if num in bits:
                continue
            cur = ""
            for i in range(31, -1,-1):
                cur += "1" if num & (1<<i) else "0"
            bits[num] = cur
            self.addNum(cur, root)

        max_res = 0
        for num in bits:
            cur_ans = 0
            current = root
            for i in range(32):
                opp = "0" if bits[num][i] == "1" else "1"
                if not current:
                    break
                elif opp in current:
                    cur_ans |= (1<<(31-i))
                    current = current[opp]
                else:
                    current = current[bits[num][i]]
            max_res = max(max_res, cur_ans)

        return max_res