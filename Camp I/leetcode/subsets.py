class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def per(cur, idx):
            subsets.append(cur[:])

            for i in range(idx, len(nums)):
                if nums[i] not in cur:
                    cur.append(nums[i])
                    per(cur, i+1)
                    cur.pop()

        per([], 0)
        
        return subsets