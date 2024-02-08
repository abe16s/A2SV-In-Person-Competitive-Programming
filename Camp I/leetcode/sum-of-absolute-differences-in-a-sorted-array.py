class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ps = [0]
        for n in nums:
            ps.append(ps[-1] + n)
        
        result = []
        for i in range(len(nums)):
            temp = nums[i] * i - ps[i]
            temp += ps[-1] - ps[i+1] - nums[i] * (len(nums)-i-1)
            result.append(temp)

        return result
