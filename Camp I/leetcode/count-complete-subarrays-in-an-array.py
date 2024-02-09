class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        goal = set(nums)
        cur = defaultdict(int)
        j = 0
        ctr = 0
        for i in range(len(nums)):
            cur[nums[i]] += 1
            while len(cur) == len(goal):
                ctr += len(nums)-i
                cur[nums[j]] -= 1
                if not cur[nums[j]]:
                    cur.pop(nums[j])
                j += 1
        return ctr