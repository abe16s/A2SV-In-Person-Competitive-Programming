class Solution:
    def printVertically(self, s: str) -> List[str]:
        maxi = 0
        s = s.split(" ")
        for i in s:
            maxi = max(maxi, len(i))
        cout = []
        for i in range(maxi):
            temp = ""
            for j in s:
                if i < len(j):
                    temp += j[i]
                else:
                    temp += " "
            cout.append(temp.rstrip())
        return cout