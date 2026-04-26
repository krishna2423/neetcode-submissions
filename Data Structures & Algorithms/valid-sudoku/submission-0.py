class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        full = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        
        cur_row = set()
        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in cur_row or board[r][c] not in full:
                    return False
                else:
                    cur_row.add(board[r][c])
            cur_row.clear()
        

        cur_col = set()
        for c in range(n):
            for r in range(n):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in cur_col or board[r][c] not in full:
                    return False
                else:
                    cur_col.add(board[r][c])
            cur_col.clear()
        

        cur_sq = set()
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] == '.':
                            continue
                        elif board[r][c] in cur_sq:
                            return False
                        else:
                            cur_sq.add(board[r][c])
                cur_sq.clear()
        
        return True


