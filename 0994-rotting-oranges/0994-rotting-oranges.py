class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        deq= deque()
        m = len(grid)
        n = len(grid[0])
        fresh =  0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 :
                    deq.append((i,j))
                elif grid[i][j] == 1 :
                    fresh += 1 
        count = 0 
        direc = [(0,-1),(1,0),(-1,0),(0,1)]
        while deq and fresh >0  :
            haha = len(deq)
            for i in range(haha):
                ni,nj = deq.popleft()
                for ix , iy in direc :
                    if 0<= ni + ix < m and 0<= nj + iy < n :
                        if grid[ni+ix][nj+iy] == 1 :
                            deq.append((ni+ix ,nj+iy))
                            grid[ni+ix][nj+iy] = 2 
                            fresh -= 1 
            count += 1 
        if fresh > 0 :
            return -1 
        return count 
