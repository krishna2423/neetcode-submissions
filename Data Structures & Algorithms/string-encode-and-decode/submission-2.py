class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            result += str(length)
            result += '#'
            result += s
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        while s:
            i = 0
            while s[i] != "#":
                i += 1
            length = int(s[:i])
            print(length)
            s = s[i+1:]
            result.append(s[0:length])
            s = s[length:]
        return result