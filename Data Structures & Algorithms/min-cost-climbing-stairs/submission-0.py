class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(idx, c):
            if idx >= len(cost):
                return c
            else:
                if idx == -1:
                    one_step = dfs(idx + 1, c)
                    two_steps = dfs(idx + 2, c)
                else:
                    one_step = dfs(idx + 1, c + cost[idx])
                    two_steps = dfs(idx + 2, c + cost[idx])
                return min(one_step, two_steps)
        return dfs(-1, 0)