class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                board_val = board[r][c]
                if board_val == ".":
                    continue
                if board_val in rows[r] or board_val in cols[c]:
                    return False
                rows[r].add(board_val)
                cols[c].add(board_val)
                box_tuple = (r//3,c//3)
                if board_val in boxes[(box_tuple)]:
                    return False 
                boxes[(box_tuple)].add(board_val)
        
        return True 