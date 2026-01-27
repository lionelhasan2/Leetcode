from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        time,fresh = 0,0
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh +=1
        while q and fresh != 0:
            for i in range(len(q)):
                x,y = q.popleft()
                for c,d in directions:
                    a = x + c
                    b = y + d               
                    if (a < 0 or a >= rows or b < 0 or b >= cols or grid[a][b] != 1):
                        continue
                    grid[a][b] = 2
                    q.append((a,b))
                    fresh -=1 
            time += 1
        return time if fresh == 0 else -1