class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += '#'
            result += s
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        curr_len = ""
        while s:
            if s[0] == '#':
                length = int(curr_len)
                curr_len = ""
                s = s[1:]
                word = s[:length]
                s = s[length:]
                result.append(word)
            else:
                curr_len += str(s[0])
                s = s[1:]
        return result
            
            
        return result
