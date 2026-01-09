class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, prevVal, visited):
            if r < 0 or c < 0:
                return (True, False)
            if r >= ROWS or c >= COLS:
                return (False, True)
            if heights[r][c] > prevVal or (r, c) in visited:
                return (False, False)
            
            visited.add((r, c))
            pacific, atlantic = False, False
            for dx, dy in directions:
                p, a = dfs(r + dx, c + dy, heights[r][c], visited)
                pacific = pacific or p
                atlantic = atlantic or a
                if pacific and atlantic:
                    break
            visited.remove((r, c))
            return (pacific, atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                pacific, atlantic = dfs(r, c, float('inf'), set())
                if pacific and atlantic:
                    res.append([r, c])
        return res