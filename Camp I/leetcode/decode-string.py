class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s, idx, f): 
            string = ""
            freq = ""
            i = idx
            stack = []
            while i < len(s):
                if s[i] == "[":
                    temp = decode(s, i+1, int(freq))
                    freq = ""
                    i = temp[1]
                    string += temp[0]
                elif s[i] == "]":
                    print(s,idx,i, f)
                    return [f * string, i]
                elif s[i].isnumeric():
                    freq += s[i]
                elif s[i].isalpha():
                    string += s[i]
                i += 1
            return [f * string, i]
        return decode(s,0, 1)[0]

        
            
        