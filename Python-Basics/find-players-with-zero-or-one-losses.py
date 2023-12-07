class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = {}
        for match in matches:
            dic[match[1]] = dic.get(match[1],0) + 1
            if match[0] not in dic:
                dic[match[0]] = 0
        print(dic)
        output = [[],[]]
        for key in dic:
            if dic[key] == 1:
                output[1].append(key)
            elif dic[key] == 0:
                output[0].append(key)
        output[0].sort()
        output[1].sort()
        return output