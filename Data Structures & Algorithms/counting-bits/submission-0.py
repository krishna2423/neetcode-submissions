class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        k = 1
        while n:
            for i in range(min(n, k)):
                res.append(res[i] + 1)
                n -= 1
            k *= 2
        return res