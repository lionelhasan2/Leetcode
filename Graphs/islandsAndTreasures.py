class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS,COLS = len(grid), len(grid[0])
        INF = 2147483647
        def bfs(r,c):
            queue = deque()
            queue.append((r,c,0))
            visited = {(r,c)}

            while queue:
                i,j,distance = queue.popleft()
                if grid[i][j] == 0:
                    return distance
                visited.add((i,j))
                
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if (0 <= ni < ROWS and 0 <= nj < COLS and 
                        (ni, nj) not in visited and grid[ni][nj] != -1):
                        queue.append((ni, nj, distance + 1))
                
            return INF
                
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)

        
            

