import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #return math.comb(m + n - 2, n - 1) #(combinatorics solution)
        cache = {}
        def dfs(r, c):
            if r < 1 or r > m or c < 1 or c > n:
                return 0
            else:
                if (r, c) in cache:
                    return cache[(r, c)]
                elif r == m and c == n:
                    return 1
                else:
                    cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
                    return cache[(r, c)]
        return dfs(1, 1)