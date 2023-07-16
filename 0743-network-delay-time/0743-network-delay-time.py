class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d={}
        for i in range(n+1):
            d[i]=[]
        for u, v, w in times:
            d[u].append((v, w))
        
        dist = [float("inf") for _ in range(n+1)]
        dist[0] = 0
        dist[k] = 0
        h=[]
        for v, w in d[k]:
            dist[v]=w
            heapq.heappush(h, (w, v))
        
        while h:
            w, v = heapq.heappop(h)
            for vi, wi in d[v]:
                if (w + wi) < dist[vi]:
                    dist[vi]=w+wi
                    heapq.heappush(h, (wi+w, vi))
        
        ans = max(dist)
        if ans==float("inf"):
            return -1
        return ans
        
        
            