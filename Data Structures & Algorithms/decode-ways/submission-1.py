class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dfs(i):
            if i >= len(s):
                return 1
            if i in cache:
                return cache[i]
            one = 0
            two = 0
            if s[i] != "0":
                one =  dfs(i + 1)
            if 10 <= int(s[i:i+2]) <= 26:
                two = dfs(i + 2) 
            cache[i] = one + two
            return cache[i]
        return dfs(0)
            
