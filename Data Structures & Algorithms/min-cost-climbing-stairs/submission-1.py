class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(idx, c, cache):
            if idx >= len(cost):
                return c
            if idx in cache:
                return cache[(idx, c)]
            else:
                one_step = dfs(idx + 1, c + cost[idx], cache)
                two_steps = dfs(idx + 2, c + cost[idx], cache)
                cache[(idx, c)] = min(one_step, two_steps)
                return cache[(idx, c)]
        return min(dfs(0, 0, {}), dfs(1, 0, {}))