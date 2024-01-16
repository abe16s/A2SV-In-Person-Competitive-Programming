class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        for i in range(len(nums)):
            if i in visited:
                continue
            current = set()      
            org = i  
            sign = nums[i] > 0
            while ((nums[i] > 0) == sign):
                if i in current:
                    return True
                if i in visited: break
                visited.add(i)
                current.add(i)
                prev = i
                i = (i + nums[i]) % len(nums)
                if prev == i: break
        return False