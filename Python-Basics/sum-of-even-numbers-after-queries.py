class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens_sum = 0
        for num in nums:
            if num % 2 == 0:
                evens_sum += num
        output = []
        for q in queries:
            if nums[q[1]] % 2 == 0 and q[0] % 2 == 0:
                evens_sum += q[0]
            elif nums[q[1]] % 2 == 1 and q[0] % 2 == 1:
                evens_sum += q[0] + nums[q[1]]
            elif nums[q[1]] % 2 == 0 and q[0] % 2 == 1:
                evens_sum -= nums[q[1]]
            nums[q[1]] += q[0]
            output.append(evens_sum)
        return output