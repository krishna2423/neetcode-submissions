class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        max_product = 1
        min_product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                max_product = 1
                min_product = 1
                continue
            tmp = max_product * nums[i]
            max_product = max(nums[i] * max_product, nums[i] * min_product, nums[i])
            min_product = min(tmp, nums[i] * min_product, nums[i])
            res = max(res, max_product)
        return res