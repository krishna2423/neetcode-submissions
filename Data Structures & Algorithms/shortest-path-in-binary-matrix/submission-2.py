from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def bfs(r, c):
            ROWS = len(grid)
            COLS = len(grid[0])
            visited = set()
            q = deque()
            
            if grid[r][c] == 1:
                return - 1 
            else:
                visited.add((r, c))
                q.append((r, c))
            
            length = 1
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()

                    if r == ROWS - 1 and c == COLS - 1:
                        return length
                    
                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [1, -1], [-1, -1], [1, 1]]

                    for dr, dc in directions:
                        row = r + dr
                        col = c + dc
                        if (col >= COLS or col < 0 or row >= ROWS or row < 0 or (row, col) in visited or
                            grid[row][col] == 1):
                            continue
                        q.append((row, col))
                        visited.add((row, col))
                length += 1
            return - 1
                    
        return bfs(0, 0)


