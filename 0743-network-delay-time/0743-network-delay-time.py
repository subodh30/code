class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d={}
        n+=1
        dist = [float("inf") for _ in range(n)]
        for i in range(n):
            d[i]=[]
        h=[]
        for u, v, w in times:
            d[u].append((v, w))
            if u == k:
                heapq.heappush(h, (w, v))
                dist[v]=w
            
        dist[0]=0
        dist[k]=0
        
        while h:
            w, u = heapq.heappop(h)
            for v, wi in d[u]:
                if wi+w < dist[v]:
                    dist[v] = wi+w
                    heapq.heappush(h, (wi+w, v))
        
        ans = max(dist)
        if ans == float("inf"):
            return -1
        return ans
        
        
            