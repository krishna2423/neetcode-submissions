from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # approach:
        # 1. find all the locations of the rotten fruits and the locations of the fresh fruits
        # 2. perform bfs from each rotten fruit at every iteration and in every iteration
        #    remove fresh fruits that are adjacent to the rotten fruit and add them to the rotten fruit
        # 3. either when the fresh fruit set becomes 0 or the fresh fruit set doesnt change after an iteration
        #    return the number of iterations or -1 respectively
        ROWS = len(grid)
        COLS = len(grid[0])

        rotten = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        def bfs(rotten):
            visited = set()
            length = -1
            while rotten:
                for i in range(len(rotten)):
                    r, c = rotten.popleft()
                    visited.add((r, c))

                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in directions:
                        row = r + dr
                        col = c + dc
                        if (row < 0 or col < 0 or row >= ROWS or col >= COLS or
                            grid[row][col] != 1 or (row, col) in visited):
                            continue
                        else:
                            grid[row][col] = 2
                            visited.add((row, col))
                            rotten.append((row, col))
                            nonlocal fresh
                            fresh -= 1
                length += 1
            return -1 if fresh > 0 else max(0, length)
        return bfs(rotten)


        
                        
