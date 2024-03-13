class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        inc_q=deque()
        min_sub=len(nums)+1
        cumul_sum=[0]
        for j in nums:
            cumul_sum.append(cumul_sum[-1] + j)
        for i,s in enumerate(cumul_sum):
            while inc_q and cumul_sum[inc_q[-1]] >= s:
                inc_q.pop()
            inc_q.append(i)

            while inc_q and s - cumul_sum[inc_q[0]] >= k:
                min_sub=min(min_sub, i-inc_q.popleft())

        return min_sub if min_sub<=len(nums) else -1 
