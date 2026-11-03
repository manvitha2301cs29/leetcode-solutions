class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        adj = [[] for i in range(n)]
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        mini = float('inf')
        h = [(0,0)]
        dist = [float('inf') for i in range(n)]
        dist[0] = 0 
        MOD = 10**9 + 7 
        ways = [0 for i in range(n)]
        ways[0] = 1
        while h :
            w , node = heapq.heappop(h)
            if w > dist[node] :
                continue 
            for ni , wi in adj[node]:
                if dist[ni] > dist[node] + wi:
                    ways[ni] = ways[node]%MOD
                    dist[ni] = w + wi
                    heapq.heappush(h,(dist[ni],ni))
                elif dist[ni] == dist[node] + wi:
                    ways[ni] = (ways[ni]+ways[node])%MOD
        return ways[n-1]

            
        