class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {}
        def dfs(idx, end):
            if idx >= end:
                return 0 
            else:
                if (idx, end) in cache:
                    return cache[(idx, end)]
                
                cache[(idx, end)] = max(nums[idx] + dfs(idx + 2, end), dfs(idx + 1, end))
                return cache[(idx, end)]
        return max(dfs(0, len(nums) - 1), dfs(1, len(nums)))
