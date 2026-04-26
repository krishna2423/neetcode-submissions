class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            b = ((n >> i) & 1)
            if b == 1:
                res = res | (1 << (31 - i))

        return res