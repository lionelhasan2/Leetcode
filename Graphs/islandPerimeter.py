class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        combinations = set()
        def perim(grid,i,j):
            # Node is water, therefore adds to the perimeter
            if i >= len(grid) or i < 0 or j>=len(grid[i]) or j<0 or grid[i][j] == 0 :
                return 1 # Add to the perimeter of the last island node if water or OOB
            if (i,j) in combinations:
                return 0 # If node has already been searched add nothing
            combinations.add((i,j))
            perimeter =  perim(grid,i+1,j) + perim(grid,i-1,j) + perim(grid,i,j+1) + perim(grid,i,j-1)
            return perimeter
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return perim(grid,i,j)
        