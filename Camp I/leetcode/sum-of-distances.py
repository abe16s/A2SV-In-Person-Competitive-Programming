class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) 
        prefix = {}
        for i in range(len(nums)):
            if nums[i] not in prefix:
                prefix[nums[i]] = [0,i,1] #distance, index, count
            else:
                d, idx, count = prefix[nums[i]]
                prefix[nums[i]][0] = (i-idx) * count + d
                prefix[nums[i]][1] = i
                prefix[nums[i]][2] += 1
                ans[i] += prefix[nums[i]][0]
        suffix = {}
        nums.reverse()
        for i in range(len(nums)):
            if nums[i] not in suffix:
                suffix[nums[i]] = [0,i,1] #distance, index, count
            else:
                d, idx, count = suffix[nums[i]]
                suffix[nums[i]][0] = (i-idx) * count + d
                suffix[nums[i]][1] = i
                suffix[nums[i]][2] += 1
                ans[len(nums)-i-1] += suffix[nums[i]][0]
        return ans


