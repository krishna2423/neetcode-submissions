class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        # get every possible substring and check if its a palindrome is a bruteforce approach
        res = 0
        # odd length palindromes
        for i in range(len(s)):
            l = i
            r = i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        # even length palindromes
        for i in range(len(s) - 1):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res