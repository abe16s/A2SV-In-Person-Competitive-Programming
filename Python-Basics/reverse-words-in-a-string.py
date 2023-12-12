class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        output = ""
        for i in range(len(s_list)-1,-1,-1):
            if s_list[i]:
                output += s_list[i] + " "
        return output.strip()