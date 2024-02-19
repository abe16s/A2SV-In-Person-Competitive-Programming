class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        goal = tickets[k]
        ctr = 0
        for i in range(len(tickets)):
            if i <= k:
                ctr += min(goal,tickets[i])
            else:
                ctr += min(goal-1,tickets[i])
        return ctr