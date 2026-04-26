class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        longest = 0 
        curr_s = ""
        while s:
            first = s[0]
            s = s[1:]
            if first in freq:
                idx = curr_s.index(first)
                curr_s = curr_s[idx+1:]
                freq = {c:1 for c in curr_s} 
            
            freq[first] = 1
            curr_s += first
            longest = max(longest, len(curr_s))
        return longest
