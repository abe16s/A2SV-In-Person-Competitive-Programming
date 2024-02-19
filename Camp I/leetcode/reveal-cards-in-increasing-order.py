class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque()
        queue.append(deck[-1])
        for i in range(len(deck)-2,-1,-1):
            queue.appendleft(queue.pop())
            queue.appendleft(deck[i])

        return queue
