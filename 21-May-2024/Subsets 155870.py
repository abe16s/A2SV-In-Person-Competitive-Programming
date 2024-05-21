# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for i in range(2**len(nums)):
            cur = []
            for j in range(len(nums)):
                if i & (1<<j):
                    cur.append(nums[j])
            subsets.append(cur)

        return subsets