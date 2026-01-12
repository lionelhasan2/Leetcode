class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        path = set()
        def backtrack(r,c,i):
            if i == len(word):
                return True
            if c>= COLS or c < 0 or r>= ROWS or r < 0:
                return False
            if (r, c) in path or board[r][c] != word[i]:
                return False
            path.add((r,c))
            for direction in directions:
                if backtrack(r+direction[0], c + direction[1], i+1):
                    return True
            path.remove((r,c))
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,0):
                    return True
        return False
    

