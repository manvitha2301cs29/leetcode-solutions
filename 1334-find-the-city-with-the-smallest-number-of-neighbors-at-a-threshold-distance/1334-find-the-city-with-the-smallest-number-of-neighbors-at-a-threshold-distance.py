class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        mat = [[float('inf') for i in range(n)] for j in range(n)]
        for u,v,w in edges :
            mat[u][v] = w 
            mat[v][u] = w 
            mat[u][u] = 0 
            mat[v][v] = 0 
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if mat[i][k] != float('inf') and mat[k][j] != float('inf') :
                        mat[i][j] = min(mat[i][j],mat[i][k]+mat[k][j])
        mini = n +1 
        city = -1 
        for i in range(n):
            count = 0 
            for j in range(n):
                if i!= j and  mat[i][j] <= distanceThreshold :
                    count += 1 
            if count <= mini :
                mini = count 
                city = i 
        return city 