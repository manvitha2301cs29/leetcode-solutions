class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        deq = deque()
        rl = [0,m-1]
        cl = [0,n-1]
        for i in rl:
            for j in range(n):
                if board[i][j] == "O":
                    deq.append((i,j))
                    board[i][j] = "T"
        for i in range(m):
            for j in cl :
                if board[i][j] == "O":
                    deq.append((i,j))
                    board[i][j] = "T"
        direc = [(-1,0),(1,0),(0,-1),(0,1)]
        while deq :
            i,j = deq.popleft()
            for dx , dy in direc:
                ni = i + dx 
                nj = j + dy 
                if 0<= ni < m and 0<= nj < n :
                    if board[ni][nj] == "O":
                        board[ni][nj] = "T"
                        deq.append((ni,nj))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
