class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def nearbyLand(grid, i, j):
            # Set the value of the land to zero
            grid[i][j] = 0
            # Look down
            if i + 1 < len(grid) and grid[i+1][j] == '1':
                nearbyLand(grid, i+1, j)
            # Right
            if j + 1 < len(grid[0]) and grid[i][j+1] == '1':
                nearbyLand(grid, i, j+1)
            # Left
            if j - 1 >= 0 and grid[i][j-1] == '1':
                nearbyLand(grid, i, j-1)
            # Up 
            if i - 1 >= 0 and grid[i-1][j] == '1':
                nearbyLand(grid, i-1, j)
        
        num_islands = 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    nearbyLand(grid, i, j)
                    num_islands += 1 
        return num_islands