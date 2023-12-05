class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = ["" for i in range(len(s))]
        for j in range(len(indices)):
            output[indices[j]] += s[j]
        return "".join(output)