class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shifting = [0] * (len(s)+1)
        for start, endd, dirr in shifts:
            if dirr:
                shifting[start] += 1
                shifting[endd+1] -= 1
            else:
                shifting[start] += 25
                shifting[endd+1] -= 25
        for i in range(1,len(shifting)):
            shifting[i] += shifting[i-1]
        cout = ""
        for i in range(len(s)):
            cout += chr(97 + (ord(s[i])-97+shifting[i])%26)

        return cout