class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        cout = ""
        while i < len(s):
            if i+2 < len(s) and s[i+2] == "#":
                cout += chr(int(s[i:i+2])+96)
                i += 3
            else:
                cout += chr(int(s[i])+96)
                i += 1
        return cout