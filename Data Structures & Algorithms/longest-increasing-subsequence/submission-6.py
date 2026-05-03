import sys
sys.setrecursionlimit(10000)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(idx, prev_idx):
            if idx >= len(nums):
                return 0
            elif (idx, prev_idx) in cache:
                return cache[(idx, prev_idx)]
            skip = dfs(idx + 1, prev_idx)

            take = 0
            if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                take = 1 + dfs(idx + 1, idx)

            cache[(idx, prev_idx)] = max(skip, take)
            return cache[(idx, prev_idx)]
        return dfs(0, -1)
