class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getD(pt):
            return (pt[0]**2 + pt[1]**2)**(1/2)
        
        hp = []
        for pt in points:
            heapq.heappush(hp, (getD(pt), pt))
        ans=[]
        while k!=0:
            ans.append(heapq.heappop(hp)[1])
            k-=1
        return ans
        