class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l-1]: continue
            for r in range(l + 1, len(nums)):
                if r > l + 1 and nums[r] == nums[r-1]: continue
                t = target - nums[l] - nums[r]
                left = r + 1
                right = len(nums) - 1
                while left < right:
                    total = nums[left] + nums[right]
                    if total == t:
                        res.append([nums[l], nums[r], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]: left += 1
                        while left < right and nums[right] == nums[right-1]: right -= 1
                        left += 1
                        right -= 1
                    elif total < t:
                        left += 1
                    else:
                        right -= 1
        return res
