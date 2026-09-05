class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direc = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        deq = deque()
        if grid[n-1][n-1] == 1 or grid[0][0] == 1 :
            return -1
        vis = set()
        vis.add((0,0))
        deq.append((1,0,0))
        while deq :
            unit , x , y = deq.popleft()
            
            if x == n-1 and y == n-1 :
                return unit 
            for dx , dy in direc :
                nx , ny = dx + x , dy + y 
                if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in vis and grid[nx][ny] == 0  :
                    deq.append((unit+1,nx,ny))
                    vis.add((nx,ny))
        return -1


