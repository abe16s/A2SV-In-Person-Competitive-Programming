class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        h = [0] * len(height)
        curMax = height[0]
        for i in range(1, len(height)):
            h[i] = curMax
            curMax = max(curMax, height[i])
        curMax = height[-1]
        h[-1] = 0
        for j in range(len(height)-2, -1,-1):
            h[j] = min(h[j], curMax)
            curMax = max(curMax, height[j])
        for i in range(len(height)):
            if h[i] > height[i]:
                rain += (h[i] -  height[i])
        return rain
