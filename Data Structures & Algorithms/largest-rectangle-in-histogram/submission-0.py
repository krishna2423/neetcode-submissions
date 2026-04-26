class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        stack.append((0, heights[0]))
        for i in range(1, len(heights)):
            if heights[i] >= stack[-1][1]:
                stack.append((i, heights[i]))
            else:
                start = stack[-1][0]
                while stack and stack[-1][1] > heights[i]:
                    elem = stack.pop()
                    area = (i - elem[0]) * elem[1]
                    if area > max_area:
                        max_area = area
                    start = elem[0]
                stack.append((start, heights[i]))
        while stack:
            elem = stack.pop()
            area = (len(heights) - elem[0]) * elem[1]
            if area > max_area:
                max_area = area
        return max_area
                