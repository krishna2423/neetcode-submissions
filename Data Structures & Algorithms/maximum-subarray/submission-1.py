class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curr = 0
        for i in range(len(nums)):
            if curr < 0:
                curr = nums[i]
            else:
                curr += nums[i]
            if curr > res:
                res = curr
        return res