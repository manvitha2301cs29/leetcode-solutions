class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        d = {}
        row = {}
        col = {}
        for i in range(9):
            row[i] = set()
            col[i] = set()
            d[i] = set()
        # (row//3)*3 + col//3 
        for r in range(9):
            for c in range(9):
                if board[r][c] in "123456789":
                    if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in d[(r//3)*3 + c//3] :
                        return False 
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    d[(r//3)*3 + c//3].add(board[r][c])
        return True



