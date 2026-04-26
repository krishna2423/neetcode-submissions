class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        curr = ""

        for i in range(len(s)):
            # add the current character at the index to curr
            curr = curr + s[i]
            # extend both ways if both characters are equal and in bounds
            j = i - 1
            k = i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                curr = s[j] + curr
                curr = curr + s[k]
                j -= 1
                k += 1
            if len(curr) > len(res):
                res = curr
            curr = ""
        
        for i in range(len(s) - 1):
            # check pairs
            l = i
            j = i + 1
            while l >= 0 and j < len(s) and s[j] == s[l]:
                curr = s[l] + curr
                curr = curr + s[j]
                l -= 1
                j += 1
            if len(curr) > len(res):
                res = curr
            curr = ""
        return res

               