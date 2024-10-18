# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        or_dict = defaultdict(int) 
        def backtrack(cur_idx, pre_or):
            if cur_idx == len(nums):
                return 
            backtrack(cur_idx+1, pre_or|nums[cur_idx])
            or_dict[pre_or|nums[cur_idx]] += 1
            backtrack(cur_idx+1, pre_or)

        backtrack(0, 0)
        return or_dict[max(or_dict)]

