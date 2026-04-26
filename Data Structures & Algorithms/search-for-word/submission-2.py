class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # check for the first letter (keep index for the first letter)
        def dfs(i, r, c):
            if i == len(word):
                return True
            if r >= len(board) or r < 0:
                return False
            if c >= len(board[0]) or c < 0:
                return False
            if board[r][c] == word[i]:
                # mark the word
                ch = board[r][c]
                board[r][c] = '#'
                found =  dfs(i + 1, r + 1, c) or dfs(i + 1, r, c + 1) or dfs(i + 1, r - 1, c) or dfs(i + 1, r, c - 1)

                board[r][c] = ch
                return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0, i, j):
                    return True
        return False

            

