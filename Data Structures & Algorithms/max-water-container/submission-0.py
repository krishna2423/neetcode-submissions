class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = float('-inf')
        p1 = 0
        p2 = len(heights) - 1

        while p1 < p2:
            curr = min(heights[p1], heights[p2]) * (p2 - p1)
            if curr > area:
                area = curr
            if heights[p1] <= heights[p2]:
                p1 += 1
            elif heights[p1] > heights[p2]:
                p2 -= 1
        return area