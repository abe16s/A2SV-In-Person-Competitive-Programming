# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        px = [0]
        for i in range(len(arr)):
            px.append(px[-1]^arr[i])
        answer = []
        for l, r in queries:
            answer.append(px[r+1]^px[l])
        return answer