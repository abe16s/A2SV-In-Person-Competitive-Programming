class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        goal = sum(nums) % p
        if not goal:
            return 0
        rs = 0
        dic = {}
        dic[0] = -1
        mini = len(nums)
        for i in range(len(nums)):
            rs += nums[i]
            key = (rs-goal)%p
            if key in dic:
                mini = min(mini, i-dic[key])
            dic[rs % p] = i


        return mini if mini < len(nums) else -1
