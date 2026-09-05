class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        vis = [False]*(n +1)
        ans = -1 
        dist = [float('inf')]*(n +1)
        dist[k] = dist[0] = 0 
        pq = [(0,k)]
        adj = [[] for i in range(n+1)]
        for u,v,w in times :
            adj[u].append((v,w))
        while pq :
            di , node = heapq.heappop(pq)
            if vis[node] :
                continue 
            vis[node] = True
            u = node  
            for v,w in adj[node]:
                if not vis[v] and dist[v] > dist[u] + w :
                    dist[v] = dist[u] + w 
                    heapq.heappush(pq,(dist[v],v))
        maxi = -1 
        for i in dist:
            if maxi < i :
                maxi = i 
        return maxi if maxi != float('inf') else -1 
