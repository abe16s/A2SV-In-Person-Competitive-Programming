class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def per(cur):
            if len(cur) == len(nums):
                permutations.append(cur[:])

            for i in range(len(nums)):
                if nums[i] not in cur:
                    cur.append(nums[i])
                    per(cur)
                    cur.pop()

        # for i in range(len(nums)):
        per([])
        
        return permutations
