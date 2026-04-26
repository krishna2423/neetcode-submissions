from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = deque(digits)
        if digits[len(digits) - 1] != 9:
                digits[len(digits) - 1] = digits[len(digits) - 1] + 1
                return list(digits)
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + carry 
                return list(digits)
            else:
                digits[i] = 0
                carry = 1
        if carry == 1:
            digits.appendleft(1)
        
        return list(digits)