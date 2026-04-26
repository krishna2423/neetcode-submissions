class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        w = False
        for i in range(1, len(height) - 1):
             # find the maximum left height and maximum right height
            max_l = max(height[:i])
            max_r = max(height[i+1:])

            area += max(0, min(max_l, max_r) - height[i])
        return area