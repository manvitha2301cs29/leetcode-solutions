class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        direc = [(-1,0),(0,1),(0,-1),(1,0)]
        m = len(heights)
        n = len(heights[0])
        heap = [(0,0,0)]
        ans = float('inf')
        vis = set()

        while heap :
            di , i,j = heapq.heappop(heap)
            if (i,j) in vis :
                continue 
            vis.add((i,j))
            if i == m -1 and j == n -1 :
                return di 
            for dx , dy in direc :
                ni , nj = i + dx , j + dy
                if 0<= ni < m and 0<= nj < n and (ni,nj) not in vis:
                    haha =  max(abs(heights[ni][nj] - heights[i][j]) , di)
                   
                    heapq.heappush(heap,(haha,ni,nj))
        return -1 
            