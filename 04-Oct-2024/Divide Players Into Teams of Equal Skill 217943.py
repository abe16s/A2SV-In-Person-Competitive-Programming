# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        nums = Counter(skill)
        equal_sum = sum(skill) // (len(skill)//2)
        chemistry = 0
        for s in skill:
            if nums[s] and nums[equal_sum-s]:
                nums[s] -= 1
                nums[equal_sum-s] -= 1
                chemistry += s*(equal_sum-s)
            elif nums[s]:
                return -1
        return chemistry