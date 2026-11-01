class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        start = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start.append([i,j])
        def isvalid(i,j,idx):
            if 0 <= i < m and 0<= j < n and idx < len(word) and  board[i][j] == word[idx] and board[i][j] != "#" :
                return True 
            return False 
        def solve(idx , i,j):
            if idx == len(word)-1:
                return True 
            val = board[i][j]
            found = False
            board[i][j] = "#"
            for dx , dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                if  isvalid(dx+i,dy+j,idx+1):
                    if solve(idx+1,dx+i,dy+j) :
                        found =  True 
                        break 
            board[i][j] = val 
            return found
        for i ,j in start :
            if solve(0,i,j):
                return True 
        return False 

            