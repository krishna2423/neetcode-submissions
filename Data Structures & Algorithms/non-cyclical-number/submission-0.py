class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n):
            s = 0
            while n:
                curr = n % 10
                s = s + (curr * curr)
                n = n // 10
            return s

        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = getSum(n)
        return True

