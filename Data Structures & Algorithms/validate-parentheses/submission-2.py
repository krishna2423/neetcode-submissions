class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []

        for c in s:
            if c in hashmap:
                stack.append(c)
            if c not in hashmap:
                if not stack:
                    return False
                if c == hashmap[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False

