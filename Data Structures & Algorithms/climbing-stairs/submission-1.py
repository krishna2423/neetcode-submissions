class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n, cache):
            if n <= 0:
                return 0 
            elif n == 1:
                return 1
            elif n == 2:
                return 2
            elif n in cache:
                return cache[n]
            else:
                cache[n] = helper(n - 1, cache) + helper(n - 2, cache)
                return cache[n]
        return helper(n, {})