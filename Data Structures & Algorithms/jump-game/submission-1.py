class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        if goal == 0:
            return True
        else:
            return False"""
        r = len(nums) - 1
        l = len(nums) - 1
        while r > 0:
            if l < 0:
                return False
            dist = r - l 
            if dist - nums[l] <= 0:
                r = l
            l -= 1
        return True