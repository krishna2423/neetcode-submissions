class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        print(wordDict)
        cache = {"":True}
        def parse(s):
            if s in cache:
                return cache[s]
            else:
                for word in wordDict:
                    if word == s[:len(word)]:
                        res = parse(s[len(word):])
                        if not res:
                            continue
                        else:
                            cache[s] = True
                            return True
                cache[s] = False
                return cache[s]
        return parse(s)