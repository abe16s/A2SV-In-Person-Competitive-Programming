# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        num = str(num)
        ones = {"1":"One", "2": "Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", 
                "8":"Eight", "9":"Nine", "0":"Zero"}
        tens = {"10":"Ten", "11": "Eleven", "12":"Twelve", "13":"Thirteen", "14":"Fourteen", "15":"Fifteen", 
                "16":"Sixteen", "17":"Seventeen", "18":"Eighteen", "19":"Nineteen", "2":"Twenty", 
                "3":"Thirty", "4": "Forty", "5":"Fifty", "6":"Sixty", "7":"Seventy", 
                "8":"Eighty", "9":"Ninety"}
        chunk = ["", "Thousand", "Million", "Billion"]
        parts = []
        j = len(num)
        for i in range(len(num)-1, -1, -1):
            if j-i == 3:
                parts.append(num[i:j])
                j = i
        if num[:j]:
            parts.append(num[:j])
        word = []
        for p in range(len(parts)):
            cur = []
            part = parts[p]
            if part == "000":
                continue
            if len(part) == 3 and part[0] != "0":
                cur.append(ones[part[0]] + " Hundred")
            if len(part) >= 2:
                if part[-2] == "0":
                    if part[-1] != "0" or (part[-1] == "0" and not cur):
                        cur.append(ones[part[-1]])
                elif part[-2] == "1":
                    cur.append(tens[part[-2]+part[-1]])
                else:
                    cur.append(tens[part[-2]])
                    if part[-1] != "0":
                        cur.append(ones[part[-1]])
            else:
                cur.append(ones[part[-1]])

            if p > 0:
                cur.append(chunk[p])
            word.append(" ".join(cur))

        return " ".join(word[::-1])