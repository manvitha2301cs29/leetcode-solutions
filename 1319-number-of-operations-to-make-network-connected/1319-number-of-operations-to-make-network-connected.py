from typing  import List
class Solution:
    class disjointset:
        def __init__(self,n):
            self.parent = [i for i in range(n)]
            self.rank = [0]*n
        def find(self,u,v):
            return self.findp(u) == self.findp(v)
        def findp(self,u):
            if self.parent[u] != u :
                self.parent[u] = self.findp(self.parent[u])
            return self.parent[u] 
        def unionbyrank(self,u,v):
            pu = self.findp(u)
            pv = self.findp(v)

            if pu == pv:
                return

            if self.rank[pu] < self.rank[pv]:
                self.parent[pu] = pv
            elif self.rank[pv] < self.rank[pu]:
                self.parent[pv] = pu
            else:
                self.parent[pv] = pu
                self.rank[pu] += 1


    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1 :
            return -1
        ds = self.disjointset(n)
        for u,v in connections:
            ds.unionbyrank(u,v)
        compo = sum(1 for i in range(n) if ds.findp(i) == i )
        return compo - 1
