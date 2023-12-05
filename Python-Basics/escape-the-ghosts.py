class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        target_dist = abs(target[0]) + abs(target[1])
        
        for r, c in ghosts:
            ghost_target = abs(target[0] - r) + abs(target[1] - c)
            if ghost_target <= target_dist:
                return False
            
        return True