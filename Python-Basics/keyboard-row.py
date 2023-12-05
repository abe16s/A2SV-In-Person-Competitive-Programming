class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        cout = []
        for w in words:
            flag = True
            temp = w
            w = w.lower()
            for i in range(3):
                if w[0] in rows[i]:
                    break
            for j in range(1,len(w)):
                if w[j] not in rows[i]:
                    flag = False
                    break
            if flag:
                cout.append(temp)
        return cout            
