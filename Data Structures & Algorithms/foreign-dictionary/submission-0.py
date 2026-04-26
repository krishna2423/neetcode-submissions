import string

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # compare adjacent words 
        # for every character make it a key in the hashmap
        # make edges for each one to letters that are lexicographically after it
        # do a topo sort
        graph = {ch: set() for word in words for ch in word}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            minLen = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""

            for j in range(minLen):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break

        visited = set()
        visiting = set()
        res = []

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return True
        
        for node in graph:
            if not dfs(node):
                return ""  # cycle detected
        return "".join(res[::-1])