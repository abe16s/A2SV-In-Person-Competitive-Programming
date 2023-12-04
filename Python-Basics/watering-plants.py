class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        x = 0
        full = capacity
        ctr = 0
        for p in plants:
            if capacity < p:
                ctr += ((x)*2)
                capacity = full
            ctr += 1
            x += 1
            capacity -= p
        return ctr
