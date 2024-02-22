class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        total = sum(nums)
        cache = {}
        def choose(left, right):
            if left > right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            f = nums[left] - choose(left+1, right)
            l = nums[right] - choose(left, right-1)

            cache[(left, right)] = max(f,l)
            return max(f,l)

        return choose(0, len(nums)-1) >= 0   
        
            

