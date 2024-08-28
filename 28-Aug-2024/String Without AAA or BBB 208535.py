# Problem: String Without AAA or BBB - https://leetcode.com/problems/string-without-aaa-or-bbb

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = ""
        turn = 0
        expected = a+b
        first, second = ["a", a], ["b",b]
        if a < b:
            first, second = ["b",b], ["a", a]
        rate = first[1]//second[1]
        rem = first[1]-second[1]
        i = 0
        while len(s) < expected:
            if turn % 2 == 0:
                if rem:
                    s += first[0] * min(first[1],2)
                    first[1] -= min(first[1],2)
                    rem -= 1
                else:
                    s += first[0] * min(rate,first[1],2)
                    first[1] -= min(rate,first[1],2)
            else:
                s += second[0] * min(1,second[1])
                second[1] -= min(1,second[1])
            turn += 1
        return s