class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n = len(points)
        mst = set()
        mst.add(tuple(points[0]))
        nonmst = set()
        for i in range(n):
            nonmst.add(tuple(points[i]))
        
        h=[]
        l=tuple(points[0])
        ans=0
        while len(mst)!=n:
            for pty in nonmst:
                d= dist(pty, l)
                heapq.heappush(h, (d, pty))
            d, pty = heapq.heappop(h)
            while pty in mst:
                d, pty = heapq.heappop(h)
            mst.add(pty)
            nonmst.remove(pty)
            ans+=d
            l=pty
        
        return ans