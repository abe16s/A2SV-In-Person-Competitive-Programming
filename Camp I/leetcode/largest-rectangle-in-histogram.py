class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        forward = [len(heights)] * len(heights)
        forward_stack = []
        for i in range(len(heights)):
            while forward_stack and heights[forward_stack[-1]] > heights[i]:
                forward[forward_stack.pop()] = i
            forward_stack.append(i)

        backward = [-1] * len(heights)
        backward_stack = []
        for i in range(len(heights)-1, -1, -1):
            while backward_stack and heights[backward_stack[-1]] > heights[i]:
                backward[backward_stack.pop()] = i
            backward_stack.append(i)

        area = 0
        for j in range(len(heights)):
            area = max(area, heights[j] * (forward[j]-backward[j]-1))

        return area

