class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = [c for c in s1]
        valid = {}
        for c in chars:
            if c in valid:
                valid[c] += 1
            else:
                valid[c] = 1
        
        l = 0 
        curr = {}
        res = False

        for r in range(len(s2)):
            if r - l == len(s1):
                if curr[s2[l]] > 1:
                    curr[s2[l]] -= 1
                else:
                    curr.pop(s2[l])
                l += 1
            if s2[r] in curr:
                curr[s2[r]] += 1
            else:
                curr[s2[r]] = 1
            if curr == valid:
                res = True

        return res


        """
        valid = set([c for c in s1])
        p = 0 
        curr = set()
        while p < len(s2) - (len(s1) - 1):
            if s2[p] in valid:
                curr.add(s2[p])
                for i in range(1, len(s1)):
                    if s2[p + i] in curr or s2[p + i] not in valid:
                        break
                    else:
                        curr.add(s2[p + i])
                if curr == valid:
                    return True
                else:
                    curr.clear()
            p += 1
        return False
        """