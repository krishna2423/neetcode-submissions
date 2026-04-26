class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while nums[i] > 0:
            nums[i] = -nums[i]
            i = abs(nums[i])
        return i
            
