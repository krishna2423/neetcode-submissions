class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        e = abs(n)
        # calculate x to the power of the absolute value of n
        res = x
        i = 1
        while i * 2 < e:
            res *= res
            i *= 2
        
        for _ in range(int(e - i)):
            res = res * x
        if n < 0:
            return 1 / res
        else:
            return res
