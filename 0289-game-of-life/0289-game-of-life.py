class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        direc = [(1,1),(1,-1),(-1,1),(0,1),(0,-1),(1,0),(-1,0),(-1,-1)]
        # we will manipulate the board , by keeping 0 as og , and next state dead , 
        # 1 og alive , next sate alive 
        # 2 og alive , next state dead
        # 3 og dead , next state alive
        for i in range(m):
            for j in range(n):
                alive = 0 
                dead = 0 
                for dx , dy in direc :
                    ni = i + dx
                    nj = j + dy
                    if 0<= ni < m and 0 <= nj < n :
                        alive += 1 if board[ni][nj] == 1 or board[ni][nj] == 2 else 0 
                        dead += 1  if board[ni][nj] == 0 or board[ni][nj] == 3 else 0 
                if board[i][j] == 1 :
                    if alive < 2 :
                        board[i][j] = 2
                    elif alive == 3 or alive == 2 :
                        board[i][j] = 1 
                    elif alive > 3  :
                        board[i][j] = 2
                else :
                    if alive == 3 :
                        board[i][j] = 3 
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2 :
                    board[i][j] = 0 
                elif board[i][j] == 3:
                    board[i][j] = 1

                



        