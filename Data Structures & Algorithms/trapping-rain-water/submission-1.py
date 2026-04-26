from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        maxLeft = [0]
        maxRight = deque([0])
        l = 0
        r = 0

        for i in range(0, len(height) - 1):
            if height[i] > l:
                l = height[i]
            maxLeft.append(l)
        
        for i in range(len(height) - 1, 0, -1):
            if height[i] > r:
                r = height[i]
            maxRight.appendleft(r)
                
        for i in range(0, len(height)):
            area += max(0, min(maxLeft[i], maxRight[i]) - height[i])
        return area