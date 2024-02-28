class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cout = []
        candidates.sort()
        def backtrack(cur, cur_sum, idx):
            if cur_sum > target:
                return
            
            if cur_sum == target:
                cout.append(cur[:])
                return
            
            for c in range(idx, len(candidates)):
                if c > idx and candidates[c] == candidates[c-1]:
                    continue
                cur.append(candidates[c])
                backtrack(cur, cur_sum+candidates[c], c+1)
                cur.pop()

        backtrack([], 0, 0)
        return cout

       