class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d={}
        n+=1
        dist = [float("inf") for _ in range(n)]
        for i in range(n):
            d[i]=[]
        #h=[]
        q=[]
        for u, v, w in flights:
            d[u].append((v, w))
            if u == src:
                #heapq.heappush(h, (w, v, 0))
                q.append((w, v, 0))
                dist[v]=w
            
        dist[src]=0
        
        while q:
            # print(q)
            # w, u, hops = heapq.heappop(h)
            w, u, hops = q.pop(0)
            hops+=1
            if hops > k:
                continue
            for v, wi in d[u]:
                if hops<=k and wi+w < dist[v]:
                    dist[v] = wi+w
                    # heapq.heappush(h, (wi+w, v, hops))
                    q.append((wi+w, v, hops))
        
        ans = dist[dst]
        if ans == float("inf"):
            return -1
        return ans
            