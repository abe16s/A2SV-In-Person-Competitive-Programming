class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = []
        current = 0
        for i in spaces:
            output.append(s[current:i])
            current = i
        output.append(s[current:])
        return " ".join(output)