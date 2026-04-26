class Node:
        def __init__(self, val, end=False):
            self.val = val
            self.end = end
            self.children = {} # maps vals to corresponding nodes

class PrefixTree:
    def __init__(self):
        self.root = Node('#')

    def insert(self, word: str) -> None:
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
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                return False
            else:
                curr = curr.children[word[i]]
            if i == len(word) - 1:
                if curr.end == False:
                    return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.children:
                return False
            else:
                curr = curr.children[prefix[i]]
        return True
        