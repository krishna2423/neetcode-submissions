class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        res = 0
        carry = 0

        a &= MASK
        b &= MASK
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            
            sum_bit = a_bit ^ b_bit ^ carry
            res |= (sum_bit << i)
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)
            
        
        if res & (1 << 31):
            return res - (1 << 32)
        return res