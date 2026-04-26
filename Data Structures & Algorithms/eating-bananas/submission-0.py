import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2

            if m == 1:
                hours = 0
                for x in piles:
                    hours += math.ceil(x / m)
                
                if hours <= h:
                    return m
                elif hours > h:
                    l = m + 1
            else: 
                t = m - 1
                hours1 = 0 
                hours2 = 0
                for x in piles:
                    hours1 += math.ceil(x / m)
                    hours2 += math.ceil(x / t)
                
                if hours1 <= h and hours2 > h:
                    return m 
                elif hours1 <= h and hours2 <= h:
                    r = m - 1
                else: 
                    l = m + 1
        return - 1