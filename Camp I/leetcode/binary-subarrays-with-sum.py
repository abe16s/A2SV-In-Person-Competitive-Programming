class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = defaultdict(int)
        dic[0] += 1
        rs = 0
        ctr = 0
        for n in nums:
            rs += n
            ctr += dic[rs-goal]
            dic[rs] += 1
        return ctr