class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_string = ""
        max_len = 0 
        seen = set()
        while s:
            curr = s[0]
            s = s[1:]
            if curr in seen:
                idx = curr_string.index(curr)
                curr_string = curr_string[idx + 1:]
                seen = {c for c in curr_string}
            
            seen.add(curr)
            curr_string = curr_string + curr
            max_len = max(max_len, len(curr_string))
        return max_len

