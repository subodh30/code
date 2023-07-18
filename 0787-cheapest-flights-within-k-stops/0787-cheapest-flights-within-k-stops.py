class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        al = {}
        dist=[]
        for i in range(n):
            al[i] = []
            dist.append(float("inf"))
        
        for s, d, p in flights:
            al[s].append((d, p))
        
        dist[src] = 0
        # h=[]
        q=[]
        for v, w in al[src]:
            dist[v]=w
            # heapq.heappush(h, (w, v, 0))
            q.append((w, v, 0))
        
        while q:
            # print(h)
            # print(dist)
            # w, v, hops= heapq.heappop(h)
            w, v, hops = q.pop(0)
            hops+=1
            if hops > k:
                continue
            
            for vi, wi in al[v]:
                if hops <= k and (wi+w) < dist[vi]:
                    # heapq.heappush(h, (wi+w, vi, hops))
                    dist[vi] = wi+w
                    q.append((wi+w, vi, hops))
                
        ans = dist[dst]
        if ans==float("inf"):
            return -1
        return ans
            