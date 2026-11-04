class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n)]
        s = k -1 
        for u,v,w in times :
            adj[u-1].append((v-1,w))
        dist = [float('inf')  for i in range(n)]
        dist[s] = 0 
        h = []
        import heapq 
        heapq.heappush(h,(0,s))
        while h :
            cos , node = heapq.heappop(h)
            if cos > dist[node]:
                continue 
            for ni , wi in adj[node]:
                if dist[ni] > cos + wi :
                    dist[ni] = cos + wi
                    heapq.heappush(h,(cos + wi,ni))
        ans = -1 
        for i in range(n):
            if dist[i] == float('inf'):
                return -1 
            else :
                ans  = max(ans,dist[i])
        return ans 

