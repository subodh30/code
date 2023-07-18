class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n = len(points)
        t=[]
        t.append(0)
        h=[]
        ans=0
        while len(t)!=n:
            for i in range(n):
                if i in t:
                    continue
                d = dist(points[t[-1]], points[i])
                heapq.heappush(h, (d, t[-1], i))
            d, i, j = heapq.heappop(h)
            while h and j in t:
                d, i ,j = heapq.heappop(h)
            t.append(j)
            ans+=d
        return ans