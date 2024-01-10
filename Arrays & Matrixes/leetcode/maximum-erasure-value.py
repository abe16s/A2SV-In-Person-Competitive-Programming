class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score  = 0
        cur = set()
        cur_sum = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] in cur:
                score = max(score, cur_sum)
                while nums[j] != nums[i]:
                    cur_sum -= nums[j]
                    cur.remove(nums[j])
                    j += 1
                cur_sum -= nums[j]
                cur.remove(nums[j])
                j += 1 
            cur_sum += nums[i]
            cur.add(nums[i])
        score = max(score, cur_sum)
        return score