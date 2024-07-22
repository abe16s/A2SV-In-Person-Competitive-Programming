# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mini = min(heights)
        size = len(heights)
        storage = [[] for i in range(max(heights)-mini+1)]
        for h in range(size):
            storage[len(storage)-heights[h]+mini-1].append(names[h])
        k = 0
        for i in storage:
            for j in i:
                names[k] = j
                k += 1
        return names


