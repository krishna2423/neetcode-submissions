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
            
            sum_bit = a_bit ^ b_bit ^ carry # either 1 bit a 1 or all bits are a 1
            res |= (sum_bit << i) # put the bit at the correct position and if its a 1 update res at that bit
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry) # at least 2 have to be 1s for there to be a carry bit
            
        
        if res & (1 << 31): # if msb is 1 that means it's 0 so we offset it by the most significant bit being 1 (half)
            return res - (1 << 32) # 2's complement
        return res