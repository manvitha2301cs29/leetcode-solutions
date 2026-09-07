class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        # indirectly asking no of groups formed 
        # we can form a group if it has same x or  y 
        # ans = n - no of groups 
        # we can find no of connected components with dfs 
        rank = [0]*n 
        par = [i for i in range(n)]
        def findp(u):
            if par[u] != u :
                par[u] = findp(par[u])
            return par[u]
        def find(u,v):
            return findp(u) == findp(v)
        def union(u,v):
            pu = findp(u)
            pv = findp(v)
            if pu == pv :
                return 
            if rank[pu] < rank[pv]:
                par[pu]  = pv 
            elif rank[pu] > rank[pv]:
                par[pv]  = pu
            else :
                par[pv]  = pu
                rank[pu] += 1 
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
        # no of roots = no of connected components 
        nr = 0 
        for i in range(n):
            if i == findp(i) :
                nr += 1 
        return n - nr 

            
