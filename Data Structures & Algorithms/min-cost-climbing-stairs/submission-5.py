class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(idx, cache):
            if idx >= len(cost):
                return 0
            if idx in cache:
                return cache[idx]
            else:
                cache[idx] = cost[idx] + min(dfs(idx + 1, cache), dfs(idx + 2, cache))
                return cache[idx]
        return min(dfs(0, {}), dfs(1, {}))