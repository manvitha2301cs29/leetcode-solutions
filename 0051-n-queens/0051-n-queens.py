class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = [["." for i in range(n) ] for j in range(n)]
        r = set()
        c = set()
        d1 = set() # r-c 
        d2 = set() # r+c 
        # state , which row i placed queen 
        # choices will be columns 
        # valid function 
        def isvalid(i,j):
            if i in r or j in c or (i+j) in d2 or (i-j) in d1 :
                return False 
            return True 
        def solve(row):
            if row == n :
                ans.append(["".join(board[i]) for i in range(n)])
                return 
            for col in range(n):
                if isvalid(row,col):
                    board[row][col] = "Q"
                    r.add(row)
                    c.add(col)
                    x = row-col
                    y = row+col
                    d1.add(x)
                    d2.add(y)
                    solve(row+1)
                    board[row][col] = "."
                    r.remove(row)
                    c.remove(col)
                    d1.remove(x)
                    d2.remove(y)
        solve(0)
        return ans 
            