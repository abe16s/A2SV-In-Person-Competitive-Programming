class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = len(cardPoints) - k
        score = float("inf")
        cur_sum = 0
        i = 0
        for j in range(len(cardPoints)):
            if j>=window:
                score = min(score, cur_sum)
                cur_sum -= cardPoints[i]
                i += 1
            cur_sum += cardPoints[j]
        score = min(score, cur_sum)
        return sum(cardPoints) - score
