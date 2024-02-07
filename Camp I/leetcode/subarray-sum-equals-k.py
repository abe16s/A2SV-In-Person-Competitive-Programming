class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        ps = [0]
        for i in range(len(nums)):
            ps.append(ps[-1]+nums[i])
        ctr = 0 
        for j in range(len(ps)):
            ctr += dic[ps[j]-k]
            dic[ps[j]] += 1
        
        return ctr