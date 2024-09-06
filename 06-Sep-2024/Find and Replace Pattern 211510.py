# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        cout = []
        for word in words:
            dic = {}
            matched = set()
            flag = True
            for i in range(len(pattern)):
                if (pattern[i] in dic and dic[pattern[i]] != word[i]) or (pattern[i] not in dic and word[i] in matched):
                    flag = False
                    break
                dic[pattern[i]] = word[i]
                matched.add(word[i])
            if flag:
                cout.append(word)
        
        return cout