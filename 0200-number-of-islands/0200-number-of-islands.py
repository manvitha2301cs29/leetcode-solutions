class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0 
        lis = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" :
                    lis.append((i,j))

        def dfs(i,j):
            if 0<= i < m and 0 <= j < n :
                if grid[i][j] == "0" :
                    return 
                grid[i][j] = "0" 
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        
        for i,j in lis :
            if grid[i][j] == "1" :
                dfs(i,j)
                count += 1 
        return count 
        