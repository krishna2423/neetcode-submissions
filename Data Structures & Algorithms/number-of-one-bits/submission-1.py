class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        count = 0
        mask = 1
        for i in range(32):
            print(n)
            r = n & mask
            mask = mask << 1
            if r != 0:
                count += 1
            
        return count
        """
        count = 0
        while n:
            count += n % 2
            n = n >> 1
        return count