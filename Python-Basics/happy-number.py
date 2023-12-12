class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return 1
        def sum_sq(n):
            total = 0
            for s in str(n):
                total += int(s)**2
            return total
        visited = {n}
        n = sum_sq(n)
        while n not in visited: 
            visited.add(n)
            if n == 1:
                return True
            n = sum_sq(n)
        return False