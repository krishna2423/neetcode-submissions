from collections import deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts_t = {}
        for i in range(len(t)):
            if t[i] in counts_t:
                counts_t[t[i]] += 1 
            else:
                counts_t[t[i]] = 1
        short_lr = (0, float('inf'))
        counts_s = {}
        l = 0 
        for r in range(len(s)):
            if s[r] in counts_s:
                counts_s[s[r]] += 1
            else:
                counts_s[s[r]] = 1
            # check if counts_s has counts_t
            while all(counts_s.get(k, 0) >= v for k, v in counts_t.items()):
                if r - l < short_lr[1] - short_lr[0]:
                    short_lr = (l, r)
                if counts_s[s[l]] == 1:
                    del counts_s[s[l]]
                else:
                    counts_s[s[l]] -= 1
                l += 1
        if short_lr[1] == float('inf'):
            return ""
        else:
            return s[short_lr[0]:short_lr[1]+1]