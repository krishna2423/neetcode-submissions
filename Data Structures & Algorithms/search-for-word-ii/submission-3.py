class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.isWord = True
        
        def dfs(r, c, root, word, visited):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or (r, c) in visited:
                return
            if board[r][c] not in root.children:
                return
            
            visited.add((r, c))
            root = root.children[board[r][c]]
            word = word + board[r][c]

            if root.isWord:
                res.add(word)
                
            dfs(r + 1, c, root, word, visited)
            dfs(r - 1, c, root, word, visited)
            dfs(r, c + 1, root, word, visited)
            dfs(r, c - 1, root, word, visited)

            visited.remove((r, c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                v = set()
                dfs(r, c, root, "", v)
        return list(res)
