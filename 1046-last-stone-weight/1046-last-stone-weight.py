class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq=[]
        for i in stones:
            heapq.heappush(hq, -i)
        
        while len(hq)>1:
            y = heapq.heappop(hq)
            x = heapq.heappop(hq)
            if y-x !=0:
                heapq.heappush(hq, y-x)
                
        return 0 if len(hq)==0 else -hq[0]
        