class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9 
        r = [set() for i in range(9)]
        c = [set() for i in range(9)]
        d =[set() for i in range(9)]
        rem = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    rem.append([i,j])
                else:
                    num = int(board[i][j])
                    r[i].add(num)
                    c[j].add(num)
                    d[(i//3)*3 + j//3].add(num)
        # (row//3)* 3 + col//3 
        def isvalid(i,j,no):
            if 0 <= i < 9 and 0 <= j < 9 and ( no in r[i] or no in c[j] or no in d[(i//3)*3 + j//3]) : 
                return False 
            return True 
        def solve(x):
            if x == len(rem):
                return True
            i,j = rem[x]
             
            for num in range(1,10):
                if isvalid(i,j,num):
                    board[i][j] = str(num)
                    r[i].add(num)
                    c[j].add(num)
                    d[(i//3)*3 + j//3].add(num)
                    if solve(x+1):
                        return True 
                    board[i][j] = "."
                    r[i].remove(num)
                    c[j].remove(num)
                    d[(i//3)*3 + j//3].remove(num)
            return False 

        solve(0)
        return board

