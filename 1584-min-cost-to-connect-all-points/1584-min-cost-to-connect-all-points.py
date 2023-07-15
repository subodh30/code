class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        

        def getDistance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1]-p2[1])
        
        mst = set()
        nonmst = set()
        for i in range(1, n):
            nonmst.add(tuple(points[i]))
        
        mst.add(tuple(points[0]))
        lastpt = tuple(points[0])
        ans = 0
        mhp = []
        while len(mst) != n:
            for y in nonmst:
                dist = getDistance(lastpt, y)
                heapq.heappush(mhp, (dist, lastpt, y))
                
            while mhp:
                mval, ptx, pty = heapq.heappop(mhp)
                if pty not in mst:
                    ans+=mval
                    mst.add(pty)
                    lastpt = pty
                    nonmst.remove(pty)
                    break
        
        return ans
        