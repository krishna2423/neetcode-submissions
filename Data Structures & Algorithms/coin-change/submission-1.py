class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(curr):
            if curr > amount:
                return float('inf')
            elif curr == amount:
                return 0
            elif curr in cache:
                return cache[curr]
            else:
                best = float('inf')
                for c in coins:
                    best = min(best, 1 + dfs(curr + c))
                cache[curr] = best
                return cache[curr]
        res = dfs(0)
        return -1 if res == float('inf') else res
        
            