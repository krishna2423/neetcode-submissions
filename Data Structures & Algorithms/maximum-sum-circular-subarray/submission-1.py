class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:    
        def kadane(nums: List[int]) -> int:
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
        
        maxSum = kadane(nums)
        minSum = -kadane([-i for i in nums])
        totalSum = sum(nums)
        if maxSum < 0:
            return maxSum
        return max(maxSum, totalSum - minSum)
        
        