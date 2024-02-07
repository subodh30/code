class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        
        def dist(p):
            return math.sqrt(p[0]**2 + p[1]**2)
        
        h = []
        for p in points:
            heapq.heappush(h, (dist(p), p))
        ans = []
        while k != 0:
            ans.append(heapq.heappop(h)[1])
            k-=1
        return ans
            