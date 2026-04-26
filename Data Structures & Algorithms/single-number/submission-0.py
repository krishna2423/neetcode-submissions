class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = nums[0]
        for i in range(1, len(nums)):
            t = t ^ nums[i]
        
        return t