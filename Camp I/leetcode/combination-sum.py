class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cout = []
        def backtrack(cur, cur_sum, idx):
            if cur_sum > target:
                return
            
            if cur_sum == target:
                cout.append(cur[:])
                return
            
            for c in range(idx, len(candidates)):
                cur.append(candidates[c])
                backtrack(cur, cur_sum+candidates[c], c)
                cur.pop()

        backtrack([], 0, 0)
        return cout