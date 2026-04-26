class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        prefixes = []
        suffix = 1
        suffixes = []
        result = []
        end = len(nums) - 1
        for i in range(len(nums)):
            prefixes.append(prefix)
            prefix *= nums[i]
            

        for i in range(len(nums)):
            suffixes.append(suffix)
            suffix *= nums[end - i]

        suffixes = suffixes[::-1]

        for i in range(len(nums)):
            result.append(suffixes[i] * prefixes[i])
        return result
        