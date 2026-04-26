class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n):
            if n <= 0:
                return 0 
            elif n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                return helper(n - 1) + helper(n-2)
        return helper(n)