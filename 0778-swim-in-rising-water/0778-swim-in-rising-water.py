class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0],0,0)]
        mini = float('inf')
        vis = set()
        direc = [(-1,0),(1,0),(0,-1),(0,1)]
        while pq :
            wi , i , j = heapq.heappop(pq)
            if i*n + j in vis :
                continue 
            vis.add(i*n + j)
            if i == n-1 and j == n -1 :
                return wi 

            

            for dx,dy in direc :
                nx,ny = i + dx , j + dy 
                if 0 <= nx < n and 0 <= ny < n and nx*n + ny not in vis:
                    haha = max(grid[nx][ny] ,wi)
                    heapq.heappush(pq,(haha,nx,ny))
        return -1
                

