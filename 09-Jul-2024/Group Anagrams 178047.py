# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = []
        for i in range(len(strs)):
            temp.append([sorted(strs[i]), i])
        temp.sort()
        cout = []
        j = 0
        while j < len(temp):
            cout.append([])
            cur = temp[j]
            while j < len(temp) and cur[0] == temp[j][0]:
                cout[-1].append(strs[temp[j][1]])
                j += 1
        return cout