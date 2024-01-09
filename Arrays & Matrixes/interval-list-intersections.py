class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] > secondList[j][1]:
                j += 1
                continue
            if secondList[j][0] > firstList[i][1]:
                i += 1
                continue
            if firstList[i][0] >= secondList[j][0]:
                output.append([firstList[i][0], min(secondList[j][1], firstList[i][1])])
            elif secondList[j][0] >= firstList[i][0]:
                output.append([secondList[j][0], min(secondList[j][1], firstList[i][1])])

            if firstList[i][1] >= secondList[j][1]:
                j += 1
            else:
                i += 1
        return output