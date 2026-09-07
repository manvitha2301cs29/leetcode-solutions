class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        c = len(connections)
        if c < n-1 :
            return -1 
        # no of operations = no of components - 1 
        # can do simple dfs to find components 
        vis = set()
        count = 0 
        adj = [[] for i in range(n)]
        for u,v in connections :
            adj[u].append(v)
            adj[v].append(u)
        def dfs(i):
            if i in vis :
                return 
            vis.add(i)
            for j in adj[i]:
                dfs(j)
        for i in range(n):
            if i not in vis :
                count += 1 
                dfs(i)
        return count -1 
            

       


