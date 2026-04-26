from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        R = len(grid)
        C = len(grid[0])

        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                for i in range(len(q)):
                    row, col = q.pop()
                    
                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbors:
                        if (min(row + dr, col + dc) < 0 or row + dr >= R or col + dc >= C or (row + dr, col + dc) in visited or 
                            grid[row + dr][col + dc] == "0"):
                            continue
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))




        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
