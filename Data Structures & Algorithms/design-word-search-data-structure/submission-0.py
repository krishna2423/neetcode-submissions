class Node:
        def __init__(self, val, end=False):
            self.val = val
            self.end = end
            self.children = {} # maps vals to corresponding nodes

class WordDictionary:

    def __init__(self):
        self.root = Node('#')

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                curr.children[word[i]] = Node(word[i])
                curr = curr.children[word[i]]
            if i == len(word) - 1:
                curr.end = True

    def search(self, word: str) -> bool:
        def dfs(curr, word, i):
            if i == len(word):
                return curr.end
            elif word[i] == '.':
                possible = []
                for c in curr.children:
                    if dfs(curr.children[c], word, i + 1):
                        possible.append(True)
                    else:
                        possible.append(False)
                return any(possible)
            elif word[i] not in curr.children:
                return False
            else:
                return dfs(curr.children[word[i]], word, i + 1)
        return dfs(self.root, word, 0)
