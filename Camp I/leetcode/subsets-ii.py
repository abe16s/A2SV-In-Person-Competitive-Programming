class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = set()
        def per(cur, idx, visited):
            subsets.add(tuple(cur))

            for i in range(idx, len(nums)):
                cur.append(nums[i])
                visited.add(i)
                per(cur, i+1, visited)
                cur.pop()
                visited.remove(i)

        per([], 0, set())
        
        return list(subsets)