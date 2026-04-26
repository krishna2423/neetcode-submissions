class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """if len(s) != len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len(sorted_s)):
            if sorted_s[i] != sorted_t[i]: 
                return False
        return True 
"""     
        if len(s) != len(t):
            return False
        ds = {}
        dt = {}
        for c in s:
            if c in ds:
                ds[c] += 1
            else:
                ds[c] = 1
        for c in t:
            if c in dt:
                dt[c] += 1
            else:
                dt[c] = 1
        if ds == dt:
            return True
        else:
            return False