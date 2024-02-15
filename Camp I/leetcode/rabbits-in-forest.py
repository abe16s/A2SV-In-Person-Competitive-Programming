class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        ctr = 0
        for k in counter:
            ctr += (math.ceil(counter[k]/(k+1))*(k+1))
        return ctr