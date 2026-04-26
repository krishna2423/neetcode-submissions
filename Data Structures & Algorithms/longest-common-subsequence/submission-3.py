class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def parser(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            elif text1[i] == text2[j]:
                cache[(i, j)] = 1 + parser(i + 1, j + 1)
    
            else:
                cache[(i, j)] = max(parser(i + 1, j), parser(i, j + 1))
            
            return cache[(i, j)]
        return parser(0, 0)