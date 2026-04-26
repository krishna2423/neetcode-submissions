class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return 0 
        frequencies = [0 for i in range(26)]

        l = 0
        res = 0
        
        for r in range(0, len(s)):
            window_len = r - l + 1
            sub = s[l: r + 1]
            for c in sub:
                idx = ord(c) - 65
                frequencies[idx] += 1
            f = max(frequencies)
            if window_len - f > k:
                frequencies[ord(s[l]) - 65] -= 1
                l += 1
            else:
                res = max(res, len(sub))
            frequencies = [0] * 26
        return res

