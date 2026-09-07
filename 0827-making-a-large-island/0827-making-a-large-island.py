class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        par = list(range(n*n))
        size = [1]*(n*n)
        ans = 0 
        sumi = 0 
        for r in grid :
            sumi += sum(r)
        if sumi == n*n :
            return sumi 
        def findp(u):
            if par[u] != u :
                par[u] = findp(par[u])
            return par[u]
        def find(u,v):
            return findp(u) == findp(v)
        def union(u,v):
            if find(u,v) :
                return 
            pu = findp(u)
            pv = findp(v)
            if size[pu] < size[pv]:
                size[pv] += size[pu]
                par[pu] = pv 
            else :
                size[pu] += size[pv]
                par[pv] = pu 
        direc = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(n):
            for j in range(n):
                index = i*n + j 
                if grid[i][j] == 1 :
                    for dx , dy in direc :
                        nx ,ny = dx + i , dy + j 
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 :
                            nei = nx*n + ny 
                            union(nei,index)
                    pn = findp(index)
                    
        for i in range(n):
            for j in range(n):
                index = i*n + j 
                
                if grid[i][j] == 0 :
                    s = set()
                    for dx , dy in direc :
                        nx ,ny = dx + i , dy + j 
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 :
                            nei = nx*n + ny 
                            pn = findp(nei)
                            s.add(pn)
                    cand = 1 
                    for iss in s :
                        cand += size[iss]
                    ans = max(ans , cand)
        return ans 



