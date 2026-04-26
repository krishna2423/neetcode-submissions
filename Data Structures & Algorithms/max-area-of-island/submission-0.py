from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        R = len(grid)
        C = len(grid[0])

        visited = set()
        result = 0 

        def bfs(r, c):
            cur_island = set()
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            cur_island.add((r, c))

            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    
                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbors:
                        if (min(row + dr, col + dc) < 0 or row + dr >= R or col + dc >= C or (row + dr, col + dc) in visited or 
                            grid[row + dr][col + dc] == 0):
                            continue
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))
                        cur_island.add((row + dr, col + dc))
            return cur_island




        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r, c) not in visited:
                    island = bfs(r, c)
                    result = max(result, len(island)) 
        return result        