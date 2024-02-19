class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxt_gtr = {}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                nxt_gtr[stack.pop()] = n
            stack.append(n)
        answer = []
        for n in nums1:
            if n in nxt_gtr:
                answer.append(nxt_gtr[n])
            else:
                answer.append(-1)
        return answer