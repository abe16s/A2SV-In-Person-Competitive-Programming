class Solution:
    def average(self, salary: List[int]) -> float:
        ma = max(salary)
        mi = min(salary)
        s = sum(salary) - ma - mi
        return s / (len(salary)-2)