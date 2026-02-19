class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ROWS,COLS = len(image), len(image[0])
        STARTCLR = image[sr][sc]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        def dfs(r,c):
            if (r,c) in visited:
                return
            
            visited.add((r,c))
            image[r][c] = color
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS):
                    if image[nr][nc] == STARTCLR:
                        dfs(nr,nc)
        
        dfs(sr,sc)
        return image
            

            