class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        v = len(graph)
        col = [-1]*v 
        def bfs(node,c):
             
            for i in graph[node]:
                if col[i] == -1 :
                    col[i] = 1 - c 
                    if not bfs(i,col[i]):
                        return False 
                else :
                    if col[i] == c :
                        return False 
            return True 
        for i in range(v):
            if col[i] == -1 :
                col[i] = 0 
                if not bfs(i,0):
                    return False 
        return True
                
