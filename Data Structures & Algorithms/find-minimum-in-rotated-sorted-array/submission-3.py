class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = float('inf')
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            result = min(result, nums[mid])
            if nums[left] < nums[right]:
                result = min(result, nums[left])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return result

