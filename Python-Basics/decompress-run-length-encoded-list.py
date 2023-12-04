class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        cout = []
        for i in range(0, len(nums), 2):
            cout += [nums[i+1]]*nums[i]
        return cout