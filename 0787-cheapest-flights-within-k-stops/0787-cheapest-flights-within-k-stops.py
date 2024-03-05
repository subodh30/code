class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = [float("inf") for _ in range(n)]
        g = {}
        for i in range(n):
            g[i] = []
        for u, v, w in flights:
            g[u].append((v, w))
            
        d[src]=0
        # print(g)
        def bfs(sv):
            q=[]
            for v,w in g[sv]:
                d[v] = w
                q.append((w, v, 0))
                
            while q:
                # print(d)
                # print(q)
                wi, u, i = q.pop(0)
                
                if d[u] >= wi:
                    d[u] = wi
                    for v, w in g[u]:
                        if i == k:
                            continue
                        q.append((d[u]+w, v, i+1))
        bfs(src)
        ans = d[dst]
        if ans == float("inf"):
            return -1
        return ans