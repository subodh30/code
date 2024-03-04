class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = [float("inf") for _ in range(n+1)]
        g = {}
        for i in range(n+1):
            g[i] = []
        for u, v, w in times:
            g[u].append((v, w))
            
        d[0]=0
        d[k]=0
        
        def bfs(sv):
            h=[]
            for v,w in g[sv]:
                heapq.heappush(h, (w, v))
                
            while h:
                wi, u = heapq.heappop(h)
                if d[u] > wi:
                    d[u] = wi
                    for v, w in g[u]:
                        heapq.heappush(h, (d[u]+w, v))
        bfs(k)
        ans = max(d)
        if ans == float("inf"):
            return -1
        return ans