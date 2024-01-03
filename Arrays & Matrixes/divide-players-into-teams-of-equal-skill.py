class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        cons = skill[0] + skill[-1] 
        chem = [skill[0]*skill[-1]]
        i = 1
        j = len(skill) - 2
        while i < len(skill)/2:
            if skill[i] + skill[j] == cons:
                chem.append(skill[i]*skill[j])
                i += 1
                j -= 1
            else:
                break
        if i-j == 1:
            return sum(chem)
        else:
            return -1

