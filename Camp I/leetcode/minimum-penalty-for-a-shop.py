class Solution:
    def bestClosingTime(self, customers: str) -> int:
        psN = [0]
        for i in range(len(customers)):
            if customers[i] == "N":
                psN.append(psN[-1]+1)
            else:
                psN.append(psN[-1])
        
        psY = [0] * (len(customers)+1)
        for i in range(len(customers)-1, -1, -1):
            if customers[i] == "Y":
                psY[i] = psY[i+1]+1
            else:
                psY[i] = psY[i+1]
        mini_hr = 0
        mini_pen = float("inf")
        for i in range(len(psN)):
            if psN[i] + psY[i] < mini_pen:
                mini_pen = psN[i] + psY[i]
                mini_hr = i
        return mini_hr
