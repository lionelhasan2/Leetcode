class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] != "O" or (i, j) in visited:
                return
            
            visited.add((i, j))
            
            for dx, dy in directions:
                dfs(i + dx, j + dy)
        
        # Mark all O's connected to borders
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1) and board[r][c] == "O":
                    dfs(r, c)
        
        # Flip: O's not in visited become X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"