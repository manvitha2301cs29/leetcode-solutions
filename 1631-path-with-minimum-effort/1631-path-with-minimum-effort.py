class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        if m ==1 and n ==1 :
            return 0 
        direc = [(-1,0),(0,-1),(0,1),(1,0)]
        h = []
        vis = set()
        heapq.heappush(h,(0,0,0))
        
        while h :
            w , x , y = heapq.heappop(h)
            if (x,y) in vis :
                continue 
            vis.add((x,y))
            
           
            if x == m -1 and y == n -1 :
                return w 
            for dx , dy in direc :
                nx = dx + x 
                ny = dy + y 
                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in vis:
                    maxi = max(w,abs(heights[nx][ny] - heights[x][y]))
                    heapq.heappush(h,(maxi,nx,ny))
        return -1 






